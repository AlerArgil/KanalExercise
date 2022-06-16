from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView


class TestView(APIView):
    permission_classes = [permissions.AllowAny, ]

    def post(self, request):
        print(request.data)
        return Response({'answer': 'answer'})
