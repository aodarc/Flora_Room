from django.contrib import admin
from FloraRoomApp import models

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    fields = ['title', 'text', 'author', 'category']
    list_filter = ['create_date']

admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Comment)
admin.site.register(models.Category)
