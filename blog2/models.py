from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
class Course(models.Model):
    
    title = models.CharField(max_length=100, blank=True, null=True)
    #content = RichTextField()  
    content = RichTextUploadingField()  
    post_date = models.DateTimeField(default=timezone.now , verbose_name ='Creation Date') 
    post_update = models.DateTimeField(auto_now = True) 
    author = models.ForeignKey(User,related_name='course' , on_delete=models.CASCADE)
    price = models.IntegerField()
    image = models.ImageField(default = 'default.jpg' , upload_to ='courses_pics')
    duree = models.IntegerField(blank=True, null=True , verbose_name ='Duration')
    is_new = models.BooleanField(default=False , verbose_name ='New Course or not')

    
    def __str__(self):
        return self.title 
    
    class Meta :
        ordering = ("-post_date",)
        
    
  

  