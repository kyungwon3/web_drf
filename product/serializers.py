from rest_framework import serializers

from product.models import Product
from review.serializers import ReviewSerializer


class ProductSerializer(serializers.ModelSerializer):
    review_set = ReviewSerializer(many=True, read_only=True)
    #상품 등록할 떄, 리뷰는 작성하지 않아도 되도록 read only 설정을 true로 해줌.
    review_count = serializers.IntegerField(source='review_set.count', read_only=True)
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'review_set', 'review_count']
        # review_set을 넣어주면 serializer가 알아서 prefetched related를 수행


