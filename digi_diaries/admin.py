from django.contrib import admin

from .models import Topic, Subtopic, Entry
admin.site.register(Topic)
admin.site.register(Subtopic)
admin.site.register(Entry)