from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('policies', views.policies, name='policies'),
    path('feedback', views.feedback, name='feedback'),
    path('requests', views.requests, name='requests'),
    path('login', views.login, name='login'),
]