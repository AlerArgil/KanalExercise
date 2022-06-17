from django.core.management.base import BaseCommand

from orders.models import create_order_from_sheet


class Command(BaseCommand):
    help = 'custom check creating order'

    def handle(self, *args, **options):
        create_order_from_sheet()
        print('do_staff')
