from django.urls import path

from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.chat_text_view, name='chat'),
    path('delete/', views.delete_history, name='delete'),
    path('image/', views.chat_image_view, name='image_chat'),
    path('delete/images/', views.delete_history_images, name='delete_images'),

    path('sound/<int:history_id>/', views.sound_message, name='sound')
]
