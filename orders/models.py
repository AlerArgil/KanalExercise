from datetime import datetime

from django.core.validators import MinValueValidator
from django.db import models

from core.models import Option
from googleapi.services import GoogleApiManipulate


class Row(models.Model):
    """
    Строка из файла sheet (обновление любого поля в строке, ведет к повторной рассылке сообщение о "сроке доставки")
    """
    id = models.PositiveBigIntegerField(primary_key=True)
    number = models.PositiveBigIntegerField()
    usd_price = models.FloatField(validators=[MinValueValidator(0)])
    delivery_time = models.DateTimeField()
    rub_price = models.FloatField(validators=[MinValueValidator(0)])
    send = models.BooleanField(default=False)

    def set_rub_price(self):
        """
        Установить значения рубля согласно текущему курсу
        :return:
        """
        self.rub_price = float(self.usd_price) * float(self.get_exchange_rate())

    def save(self, *args, **kwargs):
        """
        Установить значения рубля согласно текущему курсу и сохранить строку
        :param args:
        :param kwargs:
        :return:
        """
        self.set_rub_price()
        super().save(self, *args, **kwargs)

    def get_exchange_rate(self):
        """
        Получить значения курса доллара к рублю
        :return: float курс
        """
        exchange_rate = Option.objects.get(name='exchange_rate').value
        return exchange_rate


def create_order_from_sheet():
    """
    Парсинг файла, создание записей в таблице
    :return:
    """
    g_api = GoogleApiManipulate()
    rows = g_api.get_values()
    fields = ['id', 'number', 'usd_price', 'delivery_time']
    new_array = []
    update_array = []
    exists_array = []
    for order in rows[1:]:
        order[0] = int(order[0])
        order[1] = int(order[1])
        order[2] = float(order[2])
        order[3] = datetime.strptime(order[3], '%d.%m.%Y')
        order_array = dict(zip(fields, order))
        try:
            row = Row.objects.get(pk=order_array['id'])
            exists_array.append(order_array['id'])
            if not (row.number == order_array['number'] and row.usd_price == order_array['usd_price'] and
                    row.delivery_time == order_array['delivery_time']):
                row.set_rub_price()
                update_array.append(row)
        except Row.DoesNotExist:
            row = Row(**order_array)
            row.set_rub_price()
            new_array.append(row)
    Row.objects.exclude(id__in=exists_array).delete()
    Row.objects.bulk_create(new_array)
    Row.objects.bulk_update(update_array, ['number', 'usd_price', 'delivery_time'])
