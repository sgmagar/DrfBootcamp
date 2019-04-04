from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ["name", "price", "created_at", "updated_at"]
        read_only_fields = ["created_at", "updated_at"]


class UserSerliazer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password"]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        user = User(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
            username=validated_data["email"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
