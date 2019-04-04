from django_filters import filters
from django_filters.rest_framework import FilterSet

from api.models import Product


class ProductFilter(FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = Product
        fields = ["name"]

