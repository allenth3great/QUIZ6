from django.urls import path
from .views import register, user_login, create_post, home, approve_user

urlpatterns = [
    path('', home, name='home'),  # Add this line for the home view
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('create_post/', create_post, name='create_post'),
    path('approve_user/<int:user_id>/', approve_user, name='approve_user'),
    path('register/', register, name='register'),
]

