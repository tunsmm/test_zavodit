from django.contrib import admin

from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'body', 'image', 'tags')
    empty_value_display = '-empty-'
    list_filter = ('tags', )
    search_fields = ('title', 'body', 'tags')
