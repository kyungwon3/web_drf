from django.shortcuts import render
from rest_framework import viewsets
from order.models import Order
from order.serializers import OrderSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.admin import User
# Create your views here.

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,pid):
        if request.user == order.user:
            qs = Order.objects.all()
            serializer = OrderSerializer(qs, many=True)
            return Response(serializer.data)