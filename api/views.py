from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet

from api.filters import ProductFilter
from api.models import Product
from api.serializers import ProductSerializer, UserSerializer


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


class ProductViewset(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_class = ProductFilter


class UserViewset(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class LoginViewset(ViewSet):
    serializer_class = AuthTokenSerializer

    def create(self, request):
        '''use ObtainAuthToken APIView to validate and create a token'''
        return ObtainAuthToken().post(request)

