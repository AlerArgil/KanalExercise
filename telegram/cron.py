from itertools import repeat

from django.utils import timezone

from orders.models import Row
from telegram.models import Chat
from telegram.services import TelegramBot


def send_notification():
    """
    Рассылка сообщений о истечении срока доставки
    :return:
    """
    bot = TelegramBot()
    rows = Row.objects.filter(send=False, delivery_time__lte=timezone.now())
    message = 'У следующих номеров заказов подошел срок доставки:\n'
    for row in rows:
        message += '{},\n'.format(row.number)
        row.send = True
    if rows.count() > 0:
        rows.bulk_update(rows, ['send'])
        list(map(bot.send_notification, Chat.objects.all().values_list('chat_id', flat=True), repeat(message)))
