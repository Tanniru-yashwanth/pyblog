from django.contrib import admin
from .models import Topic, Entry, Tags, TagTopics


"""Adding the models to admin block"""
admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(Tags)
admin.site.register(TagTopics)
