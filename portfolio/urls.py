from django.urls import path
from portfolio.views import index, sobre

urlpatterns = [
    path('', index, name='index'),
    path('sobre/', sobre, name='sobre'),
]