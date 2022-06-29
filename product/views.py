from rest_framework import viewsets,status
from rest_framework.decorators import action
from rest_framework.response import Response
from product.models import Product
from product.models import Review
from product.serializers import ProductSerializer
from product.serializers import ReviewSerializer
from rest_framework.views import APIView


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        search_name = self.request.query_params.get('name',)
        if search_name:
            qs=qs.filter(name__icontains=search_name)
            
        return qs

    #custom. 'http://127.0.0.1:8000/product/search/상품'이라고 치면 상품이 들어간 항목이 나옴.
    @action(detail=False, methods=['get'],url_path="search/(?P<name>[^/.]+)")
    #(?P<name>[^/.]+) : 정규 표현식. 다양한 규칙들을 나타내는 것. -> 찾아보면 나옴
    def abc(self, request, name=None):
        qs = self.get_queryset().filter(name__icontains=name)
        serializer = self.get_serializer(qs, many=True)

        return Response(serializer.data)


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

class ReviewAPI(APIView):
    def get(self, request):
        qs = Review.objects.all()
        serializer = ReviewSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReviewSerializer(data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class ReviewDetail(APIView):
    def get(self, request, pk):
        qs = Review.objects.get(id=pk)
        serializer = ReviewSerializer(qs, many=False)
        return Response(serializer.data)

    def patch(self, request, pk):
        qs = Review.objects.get(id=pk)
        serializer = ReviewSerializer(qs, date=request.data, parsial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        qs = Review.objects.get(id=pk)
        qs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





