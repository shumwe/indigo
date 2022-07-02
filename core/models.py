from django.db import models
from django.db import models
from taggit.managers import TaggableManager
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.text import slugify
import string
import random
from django.urls import reverse
from django.contrib.auth import get_user_model
User = get_user_model()

class Path(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=255, blank=True, null=True)
    path_id = models.CharField(max_length=10, unique=True, null=True, blank=True)
    created = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name}"
    def save(self, *args, **kwargs):
        if not self.path_id:
            self.path_id = ''.join(random.choices(string.digits, k=6))
        return super(Path, self).save(*args, **kwargs)
    class Meta:
        verbose_name = "Path"
        verbose_name_plural = "Paths"
        
class Topic(models.Model):
    path = models.ForeignKey(Path, on_delete=models.CASCADE, related_name='paths')
    name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True, max_length=35, blank=True, null=True)
    description = models.TextField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return f"{self.name}"
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Topic, self).save(*args, **kwargs)
    class Meta:
        verbose_name = "Topic"
        verbose_name_plural = "Topics"

class Tutorial(models.Model, HitCountMixin):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="topics")
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=110, blank=True, null=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = TaggableManager()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')
    
    def __str__(self):
        return f"{self.title}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Tutorial, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('tutorial', kwargs={
            'path_id': self.topic.path.path_id,
            'topic_slug': self.topic.slug,
            'slug': self.slug            
        })