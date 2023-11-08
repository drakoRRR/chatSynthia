from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('signin/', views.LoginUserView.as_view(), name='login'),
    path('signup/', views.RegistrationView.as_view(), name='register'),

    path('profile/<int:pk>/', login_required(views.ProfileView.as_view()), name='profile'),

    path('logout/', LogoutView.as_view(), name='logout'),

]