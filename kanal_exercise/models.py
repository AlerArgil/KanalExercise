from django.db import models


class Option(models.Model):
    """
    Динамические настройки проекта
    """
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
