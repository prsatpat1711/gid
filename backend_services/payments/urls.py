
from django.urls import path

from .views import (
    PaymentCreate,
    PaymentList,
    PaymentRetrieveUpdateDestroyAPI
)

urlpatterns = [
    path('create/', PaymentCreate.as_view()),
    path('', PaymentList.as_view()),
    path('<int:pk>/', PaymentRetrieveUpdateDestroyAPI.as_view())
]
