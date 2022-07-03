from django.shortcuts import render
from django.views.generic.list import ListView
from hitcount.views import HitCountDetailView
from core.models import Tutorial, Topic, Path
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django_summernote.widgets import SummernoteWidget

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
    topic = Topic.objects.get(slug=topic_slug)
    tutorials = Tutorial.objects.filter(draft=False, topic=topic)
    paginator = Paginator(tutorials, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'topic': topic, 'page_obj': page_obj,
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

class CreateTutorialView(LoginRequiredMixin, CreateView):
    model = Tutorial
    fields = ['topic', 'title', 'featured_image', 'content', 'tags', 
                  'draft']
    template_name = 'core/create_tutorial.html'
    
    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
            form = super(CreateTutorialView, self).get_form(form_class)
            form.fields['content'].widget = SummernoteWidget(
                attrs={'summernote': {'width': '100%', 'height': '400px'}}
            )
            return form
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateTutorialView, self).form_valid(form)
    