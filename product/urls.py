from django.urls import path, include
from rest_framework.routers import DefaultRouter

import product.views

router = DefaultRouter()
router.register('product', product.views.ProductViewSet)



urlpatterns = [
    path('', include(router.urls)),
]