from django.shortcuts import render
from .models import Topic

def index(request):
    """Homepage for Learning Log"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Show all topics"""
    topics = Topic.object.order_by('date_added')
    context = {'topics': topics}