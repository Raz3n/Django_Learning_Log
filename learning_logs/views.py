from django.shortcuts import render

def index(request):
    """Homepage for Learning Log"""
    return render(request, 'learning_logs/index.html')