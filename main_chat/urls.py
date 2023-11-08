from django.urls import path

from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.chat_text_view, name='chat'),
]
