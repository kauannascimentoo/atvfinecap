from django.contrib import admin
from django.urls import path
from core.views import *

app_name = "core"

urlpatterns = [
    path('', IndexHomeView.as_view(), name='index'),
]