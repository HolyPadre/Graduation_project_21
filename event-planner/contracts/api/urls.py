from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('create', views.add_contract, name='add-contract'),
    path('all', views.all_contracts, name='view-contract'),
    path('update/<int:pk>', views.update_contracts, name='update-contract'),
]

