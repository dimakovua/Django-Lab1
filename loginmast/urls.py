from django.urls import path

from . import views

urlpatterns = [
    path('', views.loginmast, name='loginmast'),
]