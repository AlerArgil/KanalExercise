from django.core.management.base import BaseCommand

from core.models import Option
from orders.models import create_order_from_sheet


class Command(BaseCommand):
    help = 'get info from file'

    def handle(self, *args, **options):
        create_order_from_sheet()
        print('do_staff')
