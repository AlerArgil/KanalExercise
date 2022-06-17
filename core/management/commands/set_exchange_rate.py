from django.core.management.base import BaseCommand

from core.models import Option


class Command(BaseCommand):
    help = 'set exhange rate'

    def handle(self, *args, **options):
        Option.set_exchange_rate()
