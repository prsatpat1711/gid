
from django.urls import path

from .views import (
    CartCreate,
    CartList,
    CartRetrieveUpdateDestroyAPI
)

urlpatterns = [
    path('create/', CartCreate.as_view()),
    path('', CartList.as_view()),
    path('<int:pk>/', CartRetrieveUpdateDestroyAPI.as_view())
]
