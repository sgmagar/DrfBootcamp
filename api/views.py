from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet


class HelloAPIView(APIView):
    """
        Reference:
        https://www.django-rest-framework.org/api-guide/views/
    """

    def get(self, request):
        data = {
            "hello": "This is hello"
        }
        return Response(data)

    def post(self, request):
        pass
    def put(self, request):
        pass
    def patch(self, request):
        pass
    def delete(self, request):
        pass


class HelloViewset(ViewSet):
    """
        Reference:
        https://www.django-rest-framework.org/api-guide/viewsets/
    """

    def list(self, request):
        data = {
            "hello": "This is hello viewset"
        }
        return Response(data)
