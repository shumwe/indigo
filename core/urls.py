from django.urls import path
from core import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('path/<slug:path_id>/topics/', views.topics, name='topics'),
    path('topic/<slug:topic_slug>/tutorials/', views.tutorials_by_topic, name='tutorials'),
    path('path/<slug:path_id>/topic/<slug:topic_slug>/tutorial/<slug:slug>/', views.TutorialDetailView.as_view(), name='tutorial'),
    ]
