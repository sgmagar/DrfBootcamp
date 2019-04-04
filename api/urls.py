from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import HelloAPIView, HelloViewset, ProductViewset, UserViewset

router = DefaultRouter()
router.register("hello-viewset", HelloViewset, base_name="hello_viewset")
router.register("products", ProductViewset)
router.register("users", UserViewset)


urlpatterns = [
    path("", include(router.urls)),
    path("hello/", HelloAPIView.as_view(), name="hello")
]
