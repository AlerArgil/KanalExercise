from googleapi.models import Watcher


def refresh_watcher():
    """
    Обновить вотчер за файлом
    :return:
    """
    Watcher.refresh_watcher()
