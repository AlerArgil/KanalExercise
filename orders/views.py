from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from orders.models import create_order_from_sheet


class TestView(APIView):
    permission_classes = [permissions.AllowAny, ]

    def post(self, request):
        create_order_from_sheet()
        return Response({'answer': 'answer'})
