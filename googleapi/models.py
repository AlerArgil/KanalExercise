import datetime
import uuid

from django.conf import settings
from django.db import models
from django.utils import timezone

from googleapi.services import GoogleApiManipulate


class Watcher(models.Model):
    """
    Контроль за обновлением файла
    данные модели, данные из ответа на watch
    """
    id = models.UUIDField(primary_key=True)
    resourceId = models.CharField(max_length=30)
    resourceUri = models.CharField(max_length=300)
    expiration = models.DateTimeField()
    google_api = GoogleApiManipulate()

    @classmethod
    def refresh_watcher(cls):
        five_minute_before = (timezone.now() - datetime.timedelta(minutes=5))
        expired_soon = cls.objects.filter(expiration__lte=five_minute_before)

        if expired_soon.count() > 0 or cls.objects.all().count() == 0:
            cls.set_watch()
            for expired in expired_soon:
                expired.stop_watch()
            expired_soon.delete()

    @classmethod
    def set_watch(cls):
        """
        Старт наблюдения за файлом (для режима контроля обновления файла через google drive)
        :return: Watcher объект
        """
        service = cls.google_api.build_drive()
        body = {
            'id': str(uuid.uuid4()),
            'type': 'webhook',
            'address': settings.GOOGLE_HTTPS_URL_NOTIFY
        }
        watch = service.files().watch(fileId=settings.GOOGLE_SHEET_ID, supportsAllDrives=True, body=body)
        response = watch.execute()
        expiration_as_dt = timezone.make_aware(datetime.datetime.fromtimestamp(int(response['expiration'])/1000))
        watcher = Watcher(id=response['id'], resourceId=response['resourceId'], resourceUri=response['resourceUri'],
                          expiration=expiration_as_dt)
        watcher.save()
        return watcher

    def stop_watch(self):
        """
        Отключения наблюдение за обновлением файла в google drive
        """
        service = self.google_api.build_drive()
        body = {
                "kind": "api#channel",
                "id": str(self.id),
                "resourceId": self.resourceId,
                "resourceUri": self.resourceUri,
                "type": 'webhook',
                "address": settings.GOOGLE_HTTPS_URL_NOTIFY
            }
        service.channels().stop(body=body).execute()
