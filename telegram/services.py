import telebot
from django.conf import settings

from telegram.models import Chat


class TelegramBot:
    bot_token = settings.TELEGRAM_BOT_TOKEN
    bot = telebot.TeleBot(bot_token)

    def send_notification(self, chat_id, message):
        """
        Отправить уведомление о подошедшем (или прошедшем) сроке доставки
        :param chat_id: Идентификатор чата в который потребуется отослать сообщение
        :param message: Текст сообщения
        :return:
        """
        self.bot.send_message(chat_id, message)
        return 'OK'

    def on_start_bot(self):
        """обработка первого соощения на боте"""
        bot = self.bot

        @bot.message_handler(content_types=['text'])
        def handle_start(message):
            """
            Сохранение информации о диалоге, приветственное сообщение
            :param message: напечатанное пользователем сообщение
            :return:
            """
            msg = str(message.text)  # текст
            chat_id = message.chat.id  # id чата
            print(msg)
            if '/start' in msg:
                print('with start')
                Chat.objects.get_or_create(chat_id=chat_id)
        bot.polling(none_stop=True)
