from django.contrib import admin
from core.models import Path, Topic, Tutorial

@admin.register(Path)
class PathAdmin(admin.ModelAdmin):
    list_display = ['name', 'path_id', 'description']

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['path', 'name', 'slug', 'description']

@admin.register(Tutorial)
class TutorialAdmin(admin.ModelAdmin):
    list_display = ['title', 'topic', 'slug',]