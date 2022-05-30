from django.urls import path

from . import views

urlpatterns = [
    path('', views.take_order, name='take-order'),
    path('/take/<int:contr_id>', views.take, name='take'),
    path('/refuse/<int:contr_id>', views.refuse, name='refuse'),
]