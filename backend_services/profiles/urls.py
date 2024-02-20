
from django.urls import path

from .views import (
    ProfileCreate,
    ProfileList,
    ProfileRetrieveUpdateDestroyAPI
)

urlpatterns = [
    path('create/', ProfileCreate.as_view()),
    path('', ProfileList.as_view()),
    path('<int:pk>/', ProfileRetrieveUpdateDestroyAPI.as_view())
]
