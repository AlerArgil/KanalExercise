from django.db import models


class Watcher(models.Model):
    """
    Контроль за обновлением файла
    данные модели, данные из ответа на watch
    """
    id = models.UUIDField(primary_key=True)
    resourceId = models.CharField(max_length=30)
    resourceUri = models.CharField(max_length=300)
    expiration = models.DateTimeField()
