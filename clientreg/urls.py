from django.urls import path

from . import views

urlpatterns = [
    path('', views.clientreg, name='clientreg'),
]