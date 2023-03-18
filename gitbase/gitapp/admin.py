from django.contrib import admin
from .models import *


admin.site.register(Genre)


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'genre', 'published')
    list_display_links = ('title', 'genre')
    search_fields = ('title', 'content')


admin.site.register(News, NewsAdmin,)