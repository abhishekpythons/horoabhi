from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('horoscope/<slug:sign>/<slug:day>', views.horo)
]