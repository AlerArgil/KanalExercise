from django.db.models.signals import pre_save
from django.dispatch import receiver

from core.models import Option
from orders.models import Row


@receiver(pre_save, sender=Option)
def recalculate_order_row(sender, instance, **kwargs):
    """
    Перерасчет значений таблицы в рублях, после обновленя курса
    :param sender: Option класс
    :param instance: новый образец Option  (ждем опцию курса с её новым значением)
    :param kwargs:
    :return:
    """
    if (instance.id is not None and instance.name == 'exchange_rate' and
            Option.objects.filter(name=instance.name, value=instance.value).count() == 0):
        new_price_rows = []
        for row in Row.objects.all():
            row.set_rub_price()
            new_price_rows.append(row)
        Row.objects.bulk_update(new_price_rows, ['rub_price'])



