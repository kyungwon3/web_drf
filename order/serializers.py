from rest_framework import serializers
from order.models import Order

# 가장 기본 형태의 serializer
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
    pass
