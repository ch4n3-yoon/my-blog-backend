from django.contrib import admin

from article.models import Article as ArticleModel
from article.models import Comment as CommentModel

# Register your models here.
@admin.register(ArticleModel)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content']
    list_display_links = ['id', 'title']


@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'content']
    list_display_links = ['id', 'content']
