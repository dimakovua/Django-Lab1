from django.urls import path

from . import views

urlpatterns = [
    path('', views.homeclient, name='homeclient'),
    path('/delete-device/<int:id>', views.delete_item, name='delete-dev'),
]