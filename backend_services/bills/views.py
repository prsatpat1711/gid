from django.forms import ValidationError

from .models import Bill
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
from .serializers import BillBasicSerializer


class BillFilter(FilterSet):

    class Meta:
        model = Bill
        fields = {
            'archive':['exact']
        }

class BillCreate(ListCreateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillBasicSerializer
    permission_classes = [AllowAny]
    filter_backends = [
        filters.SearchFilter, 
        filters.OrderingFilter,
        DjangoFilterBackend
    ]
    filterset_class = BillFilter
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

class BillList(ListAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillBasicSerializer
    permission_classes = [AllowAny]
    filter_backends = [
        filters.SearchFilter, 
        filters.OrderingFilter,
        DjangoFilterBackend
    ]
    filterset_class = BillFilter
    ordering_fields = '__all__'
    search_fields = [ 
        "first_name",
        "last_name",
        "role",
        "archive"
    ]
    


class BillRetrieveUpdateDestroyAPI(RetrieveUpdateDestroyAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillBasicSerializer
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