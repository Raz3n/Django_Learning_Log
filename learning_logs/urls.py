"""Defines the url patterns for learning_logs"""

from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    # View all topics page
    path('topics/', views.topics, name='topics'),
    # View single topic
    path('topic/<int:topic_id>/', views.topic, name='topic'),
    # Page for adding a new topic
    path('new_topic/', views.new_topic, name ='new_topic'),
]