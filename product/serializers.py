from rest_framework import serializers

from product.models import Product



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price',]
        # seller는 입력받고 싶지 않아서 입력 받을 것들만 따로 정의 해주고 save 해준다 !!


