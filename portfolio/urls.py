from django.urls import path
from portfolio.views import index, sobre, todos

urlpatterns = [
    path('', index, name='index'),
    path('sobre/', sobre, name='sobre'),
    path('projetos/', todos, name='projetos'),
]