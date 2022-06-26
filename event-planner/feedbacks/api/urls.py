from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('create/', views.add_feedbacks, name='add-feedbacks'),
    path('all/', views.all_feedbacks, name='view-feedbacks'),
    path('update/<int:pk>/', views.update_feedbacks, name='update-feedback'),
    path('feedback/<int:pk>/delete/', views.delete_feedbacks, name='delete-feedback'),

]
