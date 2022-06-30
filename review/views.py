from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from review.models import Review
from review.serializers import ReviewSerializer

# class ReviewViewSet(viewsets.ModelViewSet):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#
#     def get_queryset(self):
#         qs = super().get_queryset()
#
#         search_name = self.request.query_params.get('name', )
#         if search_name:
#             qs = qs.filter(name__icontains=search_name)
#
#         return qs

class ReviewList(APIView):
    def get(self, request):
        qs = Review.objects.all()
        serializer = ReviewSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReviewSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewDetail(APIView):
    def get(self, request, pk):
        qs = Review.objects.get(id=pk)
        serializer = ReviewSerializer(qs, many=False)
        return Response(serializer.data)

    def patch(self, request, pk):
        qs = Review.objects.get(id=pk)
        serializer = ReviewSerializer(qs, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        qs = Review.objects.get(id=pk)
        qs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
