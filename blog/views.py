from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly
from . import services 

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related('author').all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]
    
    def perform_create(self, serializer):
        data = serializer.validated_data
        post = services.create_post(author=self.request.user, title=data['title'])
        serializer.instance = post
    
    def perform_update(self, serializer):
        instance = serializer.instance
        data = serializer.validated_data
        services.update_post(instance, data.get('title', instance.title)), data.get('content', instance.content)
