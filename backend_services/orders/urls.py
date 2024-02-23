
from django.urls import path

from .views import (
    OrderCreate,
    OrderList,
    OrderRetrieveUpdateDestroyAPI
)

urlpatterns = [
    path('create/', OrderCreate.as_view()),
    path('', OrderList.as_view()),
    path('<int:pk>/', OrderRetrieveUpdateDestroyAPI.as_view())
]
