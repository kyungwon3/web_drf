from rest_framework import serializers
from order.models import Order
from product.models import Product
from django.contrib.auth.models import User
from product.serializers import ProductSerializer
# 가장 기본 형태의 serializer
class OrderUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['username',]

class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price', 'seller',]

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['product'] = ProductSerializer(instance.product).data
        response['order'] = OrderUserSerializer(instance.user).data
        return response
