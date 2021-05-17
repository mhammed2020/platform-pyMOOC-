from django.db import models

# Create your models here.


class Training(models.Model) :
    img = models.ImageField(upload_to='training-pics/')
    title = models.CharField(max_length=40)
    content = models.TextField()
    
    
    
    def __str__(self) :
        
        return self.title
    