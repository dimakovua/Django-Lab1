from django.urls import path

from . import views

urlpatterns = [
    path('', views.homemaster, name='homemaster'),
    ##path('/delete-device/<int:id>', views.delete_item, name='delete-item'),
]