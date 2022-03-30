from django.db.models import fields
from rest_framework import serializers

from article.models import Article as ArticleModel
from article.models import Comment as CommentModel


class ArticleSerializer(serializers.ModelSerializer):
    createdAt = serializers.SerializerMethodField(method_name="get_created_at")
    updatedAt = serializers.SerializerMethodField(method_name="get_updated_at")
    class Meta:
        model = ArticleModel
        fields = ["id", "title", "content", "createdAt", "updatedAt"]

    def get_created_at(self, instance):
        return instance.created_at.isoformat()

    def get_updated_at(self, instance):
        return instance.updated_at.isoformat()

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = "__all__"