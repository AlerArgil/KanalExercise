from django.core.validators import MinValueValidator
from django.db import models

from kanal_exercise.models import Option


class Row(models.Model):
    """
    Строка из файла sheet (обновление любого поля в строке, ведет к повторной рассылке сообщение о "сроке доставки")
    """
    id = models.PositiveBigIntegerField(primary_key=True)
    number = models.PositiveBigIntegerField(primary_key=True)
    usd_price = models.FloatField(validators=[MinValueValidator(0)])
    delivery_time = models.DateTimeField()
    rub_price = models.FloatField(validators=[MinValueValidator(0)])

    def save(self, *args, **kwargs):
        """
        Установить значения рубля согласно текущему курсу и сохранить строку
        :param args:
        :param kwargs:
        :return:
        """
        self.rub_price = self.usd_price / self.get_exchange_rate()
        super().save(self, *args, **kwargs)

    def get_exchange_rate(self):
        """
        Получить значения курса доллара к рублю
        :return: float курс
        """
        exchange_rate = Option.objects().get(name='exchange_rate')
        return exchange_rate
