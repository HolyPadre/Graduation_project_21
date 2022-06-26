from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('create', views.add_event, name='add-event'),
    path('all', views.all_events, name='view-event'),
    path('actions/all', views.all_actions, name='view-actions'),
    path('actions/create', views.add_action,name='create-action'),
    path('update/<int:pk>', views.update_events, name='update-event'),
    path('event/<int:pk>/delete', views.delete_event, name='update-event'),

]
