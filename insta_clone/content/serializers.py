from rest_framework.serializers import ModelSerializer
from .models import UserPost, PostMedia
from create_apis.serializers import UserProfileViewSerializer

class UserPostCreateSerializer(ModelSerializer):
    
    def create(self, validate_data):
        
        # this context dictionary we are receiving from views.py
        validate_data['author'] = self.context['current_user']
        
        return UserPost.objects.create(**validate_data)
    
    class Meta:
        model = UserPost
        fields = ('caption_text', 'location', 'id', 'is_published')
        
        
class PostMediaCreateSerializer(ModelSerializer):
    
    class Meta:
        model = PostMedia
        fields = ('media_file', 'sequence_index', 'post')
        

class PostMediaViewSerializer(ModelSerializer):
    
    class Meta:
        model = PostMedia
        exclude = ('post', )
    

class PostFeedSerializer(ModelSerializer):
    
    author = UserProfileViewSerializer()
    media = PostMediaViewSerializer(many=True)   # many=True specifies multiple response, single post can have multiple media
                                                  # one to many
    class Meta:
        model = UserPost
        fields = '__all__'   # taking all fields of UserPost
        include = ('media', )          # including extra field 'media'
    