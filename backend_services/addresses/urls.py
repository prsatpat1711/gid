
from django.urls import path

from .views import (
    AddressCreate,
    AddressList,
    AddressRetrieveUpdateDestroyAPI
)

urlpatterns = [
    path('create/', AddressCreate.as_view()),
    path('', AddressList.as_view()),
    path('<int:pk>/', AddressRetrieveUpdateDestroyAPI.as_view())
]
