from django.db import models


class Chat(models.Model):
    """
    Содержит сведения о всех чатах в которые будет происходить рассылка
    """
    chat_id = models.CharField(max_length=100)
