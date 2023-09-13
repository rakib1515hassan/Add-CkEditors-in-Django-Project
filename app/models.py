from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Blog(models.Model):
    name      = models.CharField( max_length=100 )

    # Image Add করার Option আসবে না।
    content_1 = RichTextField( null=True, blank=True, config_name="default", )  

    # Image Add করার Option আসবে।   
    content_2 = RichTextUploadingField( null=True, blank=True, config_name="default", )
     

    def __str__(self):
        return self.name




## To learn more CKEditor go to =>  https://www.youtube.com/@devmaesters/playlists