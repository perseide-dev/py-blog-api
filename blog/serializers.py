from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')
    
    class Meta: 
        model = Post
        fields = ('id', 'author', 'content', 'created_at', 'updated_at', 'author_username')
        read_only_fields = ('author', 'author_username', 'created_at', 'updated_at')