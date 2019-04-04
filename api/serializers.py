from rest_framework import serializers

from api.models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ["name", "price", "created_at", "updated_at"]
        read_only_fields = ["created_at", "updated_at"]
