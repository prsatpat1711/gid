from rest_framework import serializers
from .models import Cart

class CartBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"