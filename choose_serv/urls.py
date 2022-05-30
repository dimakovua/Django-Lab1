from django.urls import path

from . import views

urlpatterns = [
    path('', views.choose, name='choose-serv'),
    path('/offer/<int:dev_id>/<int:serv_id>', views.offer, name='offer'),
]