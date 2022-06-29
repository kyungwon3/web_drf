from rest_framework import serializers

from product.models import Product
from product.models import Review


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price',]
        # seller는 입력받고 싶지 않아서 입력 받을 것들만 따로 정의 해주고 save 해준다 !!
    pass

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
    pass