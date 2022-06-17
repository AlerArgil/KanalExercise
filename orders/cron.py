from orders.models import create_order_from_sheet


def cron_create_orders():
    """
    Крон создания заказов из файла
    :return:
    """
    create_order_from_sheet()
