from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import HelloAPIView, HelloViewset

router = DefaultRouter()
router.register("hello-viewset", HelloViewset, base_name="hello_viewset")


urlpatterns = [
    path("", include(router.urls)),
    path("hello/", HelloAPIView.as_view(), name="hello")
]
