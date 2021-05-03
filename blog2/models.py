from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Course(models.Model):
    
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField()   
    post_date = models.DateTimeField(default=timezone.now ) 
    post_update = models.DateTimeField(auto_now = True) 
    author = models.ForeignKey(User,related_name='course' , on_delete=models.CASCADE)
    price = models.IntegerField()
    image = models.ImageField(default = 'default.jpg' , upload_to ='courses_pics')
    duree = models.IntegerField(blank=True, null=True)
    is_new = models.BooleanField(default=False)

    
    def __str__(self):
        return self.title 
    
  

  