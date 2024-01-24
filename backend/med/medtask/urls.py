from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("medicalChartInfoGetApi/",medicalChartInfoGetApi.as_view(), name="medicalChartInfoGetApi"),
    path("medicalCharAllocatedUserInfoGetApi/",medicalCharAllocatedUserInfoGetApi.as_view(), name="medicalCharAllocatedUserInfoGetApi"),
    path("medicalChartChangeStatus/",medicalChartChangeStatus.as_view(), name="medicalChartChangeStatus"),
    path("medicalChartStatusReset/",medicalChartStatusReset.as_view(), name="medicalChartStatusReset"),
    path("firstTimeAssingment/",firstTimeAssingment.as_view(), name="firstTimeAssingment"),
    
]