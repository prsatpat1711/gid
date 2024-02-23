
from django.urls import path

from .views import (
    ProductCreate,
    ProductList,
    ProductRetrieveUpdateDestroyAPI
)

urlpatterns = [
    path('create/', ProductCreate.as_view()),
    path('', ProductList.as_view()),
    path('<int:pk>/', ProductRetrieveUpdateDestroyAPI.as_view())
]
