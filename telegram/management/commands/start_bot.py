from django.core.management.base import BaseCommand

from telegram.services import TelegramBot


class Command(BaseCommand):
    help = 'starting bot'

    def handle(self, *args, **options):
        bot = TelegramBot()
        print('bot started')
        bot.on_start_bot()
