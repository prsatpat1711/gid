
from django.urls import path

from .views import (
    BillCreate,
    BillList,
    BillRetrieveUpdateDestroyAPI
)

urlpatterns = [
    path('create/', BillCreate.as_view()),
    path('', BillList.as_view()),
    path('<int:pk>/', BillRetrieveUpdateDestroyAPI.as_view())
]
