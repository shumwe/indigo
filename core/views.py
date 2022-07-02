from django.shortcuts import render
from django.views.generic.list import ListView
from hitcount.views import HitCountDetailView
from core.models import Tutorial, Topic, Path

def landing(request):
    top = Tutorial.objects.order_by('-hit_count_generic__hits')[:2]
    top_12 = Tutorial.objects.order_by('-hit_count_generic__hits')[:12]
    context = {'top': top, 'top_12': top_12}
    return render(request, 'core/index.html', context)

def topics(request, path_id):
    path = Path.objects.get(path_id=path_id)
    path_topics = Topic.objects.filter(path=path)
    
    
    context = {
        'path': path, 'topics': path_topics
    }
    return render(request, 'core/topics.html', context)

def tutorials_by_topic(request, topic_slug):
    #TODO: pagination
    topic = Topic.objects.get(slug=topic_slug)
    tutorials = Tutorial.objects.filter(topic=topic)
    
    context = {
        'topic': topic, 'tutorials': tutorials,
    }
    return render(request, 'core/tutorial_list.html', context)

class TutorialDetailView(HitCountDetailView):
    model = Tutorial
    template_name = 'core/tutorial_page.html'
    context_object_name = 'tutorial'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    count_hit = True
    
    def get_context_data(self, **kwargs):
        context = super(TutorialDetailView, self).get_context_data(**kwargs)
        context.update({
            'popular': Tutorial.objects.order_by('-hit_count_generic__hits')[:3],
        })
        return context