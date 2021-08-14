
from rest_framework import serializers
from blog.models import Article, Comment


class ArticleDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
          'id', 
          'title', 
          'thumbnail', 
          'slug', 
          'excerpt', 
          'body', 
          'published', 
          'author',
          'published_on'
        )
        model = Article

class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
          'title', 
          'thumbnail', 
          'excerpt', 
          'body', 
          'published',
          'author',
        )
        model = Article

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
          'id', 
          'title', 
          'thumbnail', 
          'slug', 
          'excerpt',
          'author', 
          'published_on'
        )
        model = Article

class AddCommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
          'comment', 
          'article', 
          'user',
        )
        model = Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
          'id',
          'comment', 
          'article', 
          'time',
          'user',
        )
        model = Comment