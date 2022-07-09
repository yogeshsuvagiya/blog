from django.contrib import admin
from  blog.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display=('title','description','image','date')

admin.site.register(Article ,ArticleAdmin)
