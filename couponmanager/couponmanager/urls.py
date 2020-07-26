from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', include('frontend.urls')),
    path('', include('coupon.urls')),
]
