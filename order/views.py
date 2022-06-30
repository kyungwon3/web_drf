from django.shortcuts import render
from rest_framework import viewsets
from order.modes import Order
# Create your views here.

class OrderViewSet(viewsets.ModelViewSet):
    quaryset = Order.objects.all()
    serializer_class = OrderSerializer