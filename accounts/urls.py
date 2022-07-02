from django.urls import path
from accounts import views

urlpatterns = [
    path('profile/<slug:username>/', views.profile, name='profile'),
]