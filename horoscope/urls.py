from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('horoscope/',views.chooseZodiac),
    path('horoscope/<slug:sign>/<slug:day>', views.horo),
    path('images/', views.imgs),
    path('quotes/', views.quotes)
]