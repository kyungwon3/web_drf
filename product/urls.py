from django.urls import path, include
from rest_framework.routers import DefaultRouter

import product.views

# router = DefaultRouter()
# router.register('product', product.views.ProductViewSet)



urlpatterns = [

    # path('', include(router.urls)),
    path('review/', product.views.ReviewAPI.as_view()),
    path('review/<int:pk>/', product.views.ReviewDetail.as_view()),

    ]