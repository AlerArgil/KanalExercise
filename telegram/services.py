# -*- coding: utf-8 -*-
"""

"""
from urllib.parse import unquote

import telebot
from PIL import Image
from constance import config
# в настройках сайта расположить
# bot = 'kepvi_bot'
# bot = 'kepvi_testbot'
# bot_token = '980147444:AAHcNV5jiUIepjQzq9c00nAbE-Dp842Rpzk'
# bot_token = '1487952088:AAFYFGSmYJ8-E4nNbiSQiah3buHyZFnTtUk'
from django.conf import settings
from django.contrib.staticfiles.finders import find

from kepvi.account.models import Profile





# для имитации работы бота
user_token = 0

class TelegramBot:
    bot_token = config.TELEGRAM_BOT_TOKEN
    bot = telebot.TeleBot(bot_token)

    def send_notification(self, chat_id, image, from_user_name, from_gender, message_url, anketa_url, static=False):
        '''Пример отправки уведомления пользователю. Надо подставить, полученный и
        сохраненный в ходе подключения ID пользователя.
        Далее для примера, указан id чата c @kepvicom, имя от кого = Анастасия, пол = Женский'''
        bot_token = config.TELEGRAM_BOT_TOKEN
        bot = telebot.TeleBot(bot_token)
        if from_gender == 'female':
            notification_text = f'{from_user_name}, написала вам сообщение'
        else:
            notification_text = f'{from_user_name}, написал вам сообщение'
        markup_keys = telebot.types.InlineKeyboardMarkup()  # создаем кнопки
        markup_keys.row_width = 1
        markup_keys.add(telebot.types.InlineKeyboardButton("Посмотреть сообщение", url=message_url),
                        telebot.types.InlineKeyboardButton("Открыть анкету", url=anketa_url))
        if static:
            directory = settings.STATICFILES_DIRS[0]
        else:
            directory = settings.MEDIA_ROOT
        opened_image = Image.open(directory + unquote(image))
        bot.send_photo(chat_id, opened_image, caption=notification_text, reply_markup=markup_keys)
        opened_image.close()
        return 'OK'

    def start_bot(self):
        # send_notification(666070854, 'Ат', 'female') #тест отправки уведомлений
        self.bot.send_message(666070854, 'Ат')
        self.bot.polling(none_stop=True)

