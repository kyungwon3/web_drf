from rest_framework import serializers
from review.models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['score','contents',]
        #writer는 입력 안해도 되도록 해줌.
    pass