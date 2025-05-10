from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    path('submit/', views.submit_mood, name='submit_mood'),
    path('history/', views.mood_history, name='mood_history'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    # If you want to make /accounts/profile/ redirect to the same profile page
    path('accounts/profile/', views.profile, name='default_profile'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    # Other paths like login and logout can be added if necessary
]
