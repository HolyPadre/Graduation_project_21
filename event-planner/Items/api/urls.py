from django.urls import path, include
from .views import ItemViewSet
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("items", ItemViewSet, basename="Items")

urlpatterns = [
    path('', include(router.urls)),
    path('types', views.all_type, name='view-types'),
    path('types_filter', views.all_item_has_type, name='view-types'),
    path('customerItems', views.all_item_by_location_and_type, name='view-types'),
    path('item', views.all_item_by_name, name='view-types'),
    path('requests', views.all_requests, name='view-types'),
    path('price/acs', views.all_item_by_price_ASC, name='view-types'),
    path('price/desc', views.all_item_by_price_DESC, name='view-types'),
    path('mostRated', views.all_item_Most_rated, name='view-types'),
    path('capicty', views.all_item_capisty, name='view-types'),
    path('times/<int:pk>', views.returnAvalibleTime, name='times'),
    path('reserved/delete/<int:pk>', views.delete_request, name='times'),
    path('request/<int:pk>', views.updateAvalibleTime, name='updateAvalibleTime'),
    path('request/create', views.add_request, name='add_request'),

]
