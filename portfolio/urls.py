from django.urls import path
from portfolio.views import index, sobre, todos, invasão_espacial, site_portfolio, bot_automacao, mearm
urlpatterns = [
    path('', index, name='index'),
    path('sobre/', sobre, name='sobre'),
    path('projetos/', todos, name='projetos'),

    # paths das páginas dos projetos
    path('invasão_espacial/', invasão_espacial, name='invasao_espacial'),
    path('site_portfolio/', site_portfolio, name='site_portfolio'),
    path('bot_automacao/', bot_automacao, name='bot_automacao'),
    path('mearm/', mearm, name='mearm'),
    
]