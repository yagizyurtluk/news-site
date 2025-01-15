from django.contrib import admin
from .models import News, Editor

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'pub_date', 'editor')
    search_fields = ('title', 'content')
    list_filter = ('pub_date', 'category')
    date_hierarchy = 'pub_date'
    ordering = ('-pub_date',)

admin.site.register(News, NewsAdmin)
admin.site.register(Editor)
