from .models import UserPost, PostMedia
from .serializers import UserPostCreateSerializer, PostMediaCreateSerializer
from .serializers import PostFeedSerializer
from .filters import CurrentUserFollowingFilterBackend

from rest_framework import generics, mixins
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.permissions import IsAuthenticated
# Create your views here.


# Steps are,
# 1. We create a post without any content and send back the post id.
# 2. We use the post id, and sequence_index and media file to upload the post.
# 3. Update the post and publish


class UserPostCreateFeed(mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         generics.GenericAPIView):
    
    permission_classes = [IsAuthenticated,]
    authentication_classes = [JWTAuthentication, ]
    
    queryset = UserPost.objects.all()
    serializer_class = UserPostCreateSerializer
    filter_backends = [CurrentUserFollowingFilterBackend, ]
    
    # TODO: Create a system to follow topics or hashtags
    # TODO: Create a way of ordering the feeds - based on post popularity
    
    # using this method we send some extra data to the serializer
    def get_serializer_context(self):
        # this is the serializer context object, that we receive in serializer class
        return {'current_user': self.request.user.profile}
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PostFeedSerializer
        return self.serializer_class
    
    # for using create we will have to import mixins.CreateModelMixin
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
        
    
class PostMediaView(mixins.CreateModelMixin, generics.GenericAPIView):
    
    permission_classes = [IsAuthenticated,]
    authentication_classes = [JWTAuthentication, ]
    
    queryset = PostMedia.objects.all()
    serializer_class = PostMediaCreateSerializer
    
    # should be made idempotent
    def put(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class UserPostDetailUpdateView(mixins.UpdateModelMixin, 
                               mixins.RetrieveModelMixin,
                               generics.GenericAPIView):
    
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [JWTAuthentication, ]
    serializer_class = UserPostCreateSerializer
    
    queryset = UserPost.objects.all()
    
    def get_serializer_class(self):
        if self.request.method =='GET':
            return PostFeedSerializer
        
        return self.serializer_class
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
        