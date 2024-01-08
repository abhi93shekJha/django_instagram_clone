from django.db import models
from create_apis.models import AbstractTimeStamp, UserProfile

# Steps are,
# 1. We create a post without any content and send back the post id.
# 2. Frontend will now upload the media, for which request will send post id, and sequence_index and media file to upload the post.
# 3. Update the post and publish, as soon as the user submits the post.

# Create your models here.
class UserPost(AbstractTimeStamp):
    
    caption_text = models.CharField(max_length=255, null=True)
    # TODO: Store LAT LONG instead of string
    location = models.CharField(max_length=255, null=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE,
                               related_name='post')
    
    # will be used when the media files are published, should be set on the backend but for this project,
    # we are allowing frontend to set this
    is_published = models.BooleanField(default=False)
    

class PostMedia(AbstractTimeStamp):
    
    def media_name(instance, filename):
        ext = filename.split(".")[-1]
        # TODO implement a UUID instead of interger post id
        return f'post_media/{instance.post.id}_{instance.sequence_index}.{ext}'
    
    media_file = models.FileField(upload_to=media_name)
    
    sequence_index = models.PositiveSmallIntegerField(default=0)   # value can be in between 0 and 2^15-1
    post = models.ForeignKey(UserPost, on_delete=models.CASCADE,
                             related_name='media')
    
    class Meta:
        unique_together = ('sequence_index', 'post')
    
        