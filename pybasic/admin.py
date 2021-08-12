from django.contrib import admin
from .models import Topic, Entry

"""Adding the models to admin block"""
admin.site.register(Topic)
admin.site.register(Entry)
