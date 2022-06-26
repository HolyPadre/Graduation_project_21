from django.urls import path
from . import views

urlpatterns = [
    path('create', views.add_guests, name='add-guests'),
    path('all', views.view_guests, name='view-guests'),
    path('update/<int:pk>', views.update_guests, name='update-guests'),
    path('get/<int:event>', views.ViewGuestsByEventId, name='get-guests-by-event-id'),
    path('guest/<int:pk>/delete', views.delete_guests, name='delete-guest'),
    path('send', views.email, name=''),
    # path('sendsms', views.Score, name=''),

]
