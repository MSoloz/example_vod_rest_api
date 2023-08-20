from django.urls import path
from . import views

urlpatterns = [
    path('video/create/', views.create_video, name='create_video'),
    path('video/update/<int:pk>/', views.update_video, name='update_video'),
    path('video/all/', views.get_all_videos, name='get_all_videos'),
    path('video/<int:pk>/', views.get_video_by_id, name='get_video_by_id'),
    path('video/delete/<int:pk>/', views.delete_video, name='delete_video'),
]