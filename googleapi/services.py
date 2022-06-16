import uuid

from django.conf import settings
from googleapiclient.discovery import build


"""
Необходимые манипуляции с google api
"""


class GoogleApiManipulate:
    creds = settings.GOOGLE_CREDS
    sheet = settings.GOOGLE_SHEET_ID

    def _build_service(self, service: str, version: str):
        """
        Создать образец одного из google сервисов
        :param service:  наименование сервиса
        :param version:  версия сервиса
        :return: сервис
        """
        return build(service, version, credentials=self.creds)

    def build_drive(self):
        """
        Создать образец сервиса работы с google drive
        :return: сервис работы с google drive
        """
        return self._build_service('drive', 'v3')

    def build_sheets(self):
        """
        Создать образец сервиса работы с google sheets
        :return: сервис работы с google sheets
        """
        return self._build_service('sheets', 'v4')

    def get_values(self):
        """
        Получение содержимого sheet документа в столбац с A до D
        :return: list с строками из файла
        """
        service = self.build_sheets()
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=self.sheet, range='A:D').execute()
        return result.get('values', [])

    def set_watch(self):
        """
        Старт наблюдения за файлом (для режима контроля обновления файла через google drive)
        :return: response от google drive
        """
        service = self.build_drive()
        body = {
            'id': str(uuid.uuid4()),
            'type': 'webhook',
            'address': settings.GOOGLE_HTTPS_URL_NOTIFY
        }
        watch = service.files().watch(fileId=settings.GOOGLE_SHEET_ID, supportsAllDrives=True, body=body)
        return watch.execute()

    def stop_watch(self, watcher):
        """
        Отключения наблюдение за обновлением файла в google drive
        :param watcher: Объект Watcher от которого следует отключить наблюдение
        """
        service = self.build_drive()
        body = {
                "kind": "api#channel",
                "id": watcher.id,
                "resourceId": watcher.resourceId,
                "resourceUri": watcher.resourceUri,
                "type": 'webhook',
                "address": settings.GOOGLE_HTTPS_URL_NOTIFY
            }
        service.channels().stop(body=body).execute()
