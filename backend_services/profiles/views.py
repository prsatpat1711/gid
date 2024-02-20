from django.forms import ValidationError

from .models import Profile
from django.shortcuts import render
from rest_framework.response import Response

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import (
    ListCreateAPIView, 
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
)
from django_filters import (
    FilterSet,
    CharFilter,
    BooleanFilter
)

from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import ProfileBasicSerializer


class ProfileFilter(FilterSet):

    class Meta:
        model = Profile
        fields = {
            'first_name': ['iexact'],
            'last_name':['iexact'],
            'role': ['exact'],
            'archive':['exact']
        }

class ProfileCreate(ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileBasicSerializer
    permission_classes = [AllowAny]
    filter_backends = [
        filters.SearchFilter, 
        filters.OrderingFilter,
        DjangoFilterBackend
    ]
    filterset_class = ProfileFilter
    ordering_fields = '__all__'
    search_fields = [ 
        "first_name",
        "last_name",
        "role",
        "archive"
    ]

    def perform_create(self, serializer):
        if self.request.user:
            instance = serializer.save(
                created_by=self.request.user,
                updated_by=self.request.user
            )
        else:
            instance = serializer.save()

class ProfileList(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileBasicSerializer
    permission_classes = [AllowAny]
    filter_backends = [
        filters.SearchFilter, 
        filters.OrderingFilter,
        DjangoFilterBackend
    ]
    filterset_class = ProfileFilter
    ordering_fields = '__all__'
    search_fields = [ 
        "first_name",
        "last_name",
        "role",
        "archive"
    ]
    

class ProfileRetrieveUpdateDestroyAPI(RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileBasicSerializer
    permission_classes = [AllowAny]
    
    def perform_destroy(self, instance):
        instance.archive = True
        instance.updated_by = self.request.user
        instance.save()
    
    def perform_update(self, serializer):
        if self.request.user:
            instance = serializer.save(
                updated_by=self.request.user
            )
        else:
            instance = serializer.save()
        return instance