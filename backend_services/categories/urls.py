
from django.urls import path

from .views import (
    CategoryCreate,
    CategoryList,
    CategoryRetrieveUpdateDestroyAPI
)

urlpatterns = [
    path('create/', CategoryCreate.as_view()),
    path('', CategoryList.as_view()),
    path('<int:pk>/', CategoryRetrieveUpdateDestroyAPI.as_view())
]
