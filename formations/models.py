from django.db import models

# Create your models here.


class Training(models.Model) :
    title = models.CharField(max_length=40)
    content = models.TextField()
    img = models.ImageField(upload_to='training-pics/')

    

    def __str__(self) :
        
        return self.title


class Course(models.Model):
    
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField() 
    training = models.ForeignKey(Training,related_name='course' , on_delete=models.CASCADE)
    image = models.ImageField(upload_to ='courses_for_pics')
 
    def __str__(self):
        return self.title 

        
    
  

  