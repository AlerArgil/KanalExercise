from django.core.management.base import BaseCommand

from googleapi.models import Watcher


class Command(BaseCommand):
    help = 'set watcher on file'

    def handle(self, *args, **options):
        """
        Создать ватчер за файлом
        :param args:
        :param options:
        :return:
        """
        Watcher.set_watch()
        print('done')
