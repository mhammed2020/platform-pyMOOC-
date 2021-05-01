from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model) :

    user = models.OneToOneField(User, related_name='pp', on_delete=models.CASCADE)
    img = models.ImageField( default = 'default.jpg',upload_to = "pics/")
    
    # for User ,, objp=P() ,  obju= User() objp.user.username....add()   , obju.pp.ima.   -- > 
    
    def __str__(self) :
        
        return  '{} Profile'.format(self.user.username)

# @receiver(post_save, sender=User)

def create_profile(sender,**kwargs) :
    print(sender,"*** sender sender ",kwargs)
    if kwargs['created']  :
        # print(sender,instance,created,"***************")
        Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile,sender=User)