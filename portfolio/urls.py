from django.urls import path
from portfolio.views import index, sobre

urlpatterns = [
    path('', index),
    path('sobre/', sobre)
]