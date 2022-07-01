from django.shortcuts import render
from django.views.generic.list import ListView
from hitcount.views import HitCountDetailView
from core.models import Tutorial, Topic, Path


def landing(request):
    return render(request, 'core/index.html')

def topics(request, path_id):
    path = Path.objects.get(path_id=path_id)
    path_topics = Topic.objects.filter(path=path)
    
    context = {
        'path': path, 'topics': path_topics
    }
    return render(request, 'core/topics.html', context)

def tutorials_by_topic(request, topic_slug):
    topic = Topic.objects.get(slug=topic_slug)
    tutorials = Tutorial.objects.filter(topic=topic)
    
    context = {
        'topic': topic, 'tutorials': tutorials,
    }
    return render(request, 'core/tutorial_list.html', context)