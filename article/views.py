from django.db import models
from rest_framework.views import APIView
from rest_framework import permissions

from util import response
from util import crypto

from article.models import Article as ArticleModel
from article.models import Comment as CommentModel
from article.serializer import ArticleSerializer
from article.serializer import CommentSerializer


class Article(APIView):
    def get(self, request, article_id=None):
        if article_id is not None:
            try:
                article = ArticleModel.objects.get(id=article_id)
            except ArticleModel.DoesNotExist:
                return response.fail("no such article")
            
            return response.success(article)
        
        all = request.GET.get("all", "")
        if all:
            articles = ArticleModel.objects.all()
            return response.success(articles)
    
    def post(self, request):
        title = request.POST.get("title", "")
        content = request.POST.get("content", "")
        
        article = ArticleModel.objects.create(title=title, content=content)
        return response.success(article)

    def put(self, request, article_id=None):
        if article_id is None:
            return response.fail("article_id was not provided")
        
        title = request.POST.get("title", "")
        content = request.POST.get("content", "")
        
        try:
            article = ArticleModel.objects.get(id=article_id)
        except ArticleModel.DoesNotExist:
            return response.fail("no such article")

        article.title = title 
        article.content = content
        
        article.save()
        
        return response.success(article)


class Comment(models.Model):
    def get(self, request, article_id, comment_id=None):
        try:
            article = ArticleModel.objects.get(id=article_id)
        except ArticleModel.DoesNotExist:
            return response.fail("no such article")
        
        comments = CommentModel.objects.filter(article=article)
        return response.success(comments)

    def post(self, request, article_id):
        try:
            article = ArticleModel.objects.get(id=article_id)
        except ArticleModel.DoesNotExist:
            return response.fail("no such article")
        
        nickname = request.POST.get("nickname", "")
        password = request.POST.get("password", "")
        content = request.POST.get("content", "")
        
        hashed_password = crypto.sha256(password)
        
        comment = CommentModel.objects.create(
            article=article,
            nickname=nickname,
            password=hashed_password,
            content=content,
        )
        
        return response.success(comment)

    def put(self, request, comment_id=None):
        if not comment_id:
            return response.fail("comment_id was not provided")

        password = request.POST.get("password", "")
        hashed_password = crypto.sha256(password)

        try:
            comment = CommentModel.objects.get(id=comment_id)
        except CommentModel.DoesNotExist:
            return response.fail("no such comment")

        if comment.password != hashed_password:
            return response.fail("password is not correct")

        return response.success(comment)
        