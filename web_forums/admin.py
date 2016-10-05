from django.contrib import admin

# Register your models here.

from web_forums.models import Topic, Entry

admin.site.register(Topic)
admin.site.register(Entry)

#register your admin page action here