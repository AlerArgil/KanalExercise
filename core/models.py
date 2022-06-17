import requests
import xml.etree.ElementTree as ET

from django.conf import settings
from django.db import models


class Option(models.Model):
    """
    Динамические настройки проекта
    """
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200)

    @classmethod
    def set_exchange_rate(cls):
        xml_response = requests.get(settings.CB_LINK)
        root = ET.fromstring(xml_response.content)
        item = 'Valute[@ID="{}"]'.format(settings.CB_DOLLAR_ID)
        for el in root.find(item):
            if el.tag == 'Value':
                exchange_rate = float(el.text.replace(',', '.'))
        try:
            cls.objects.update_or_create(
                name='exchange_rate',
                defaults={'value': exchange_rate}
            )
        except NameError:
            pass
