from django.shortcuts import render
from . models import Training
# Create your views here.

def list_view(request) :
    
    return render(request,'formations/list_view.html',{'training' :Training.objects.all()})





def training_course(request,slug) :
    user = Training.objects.get(slug = slug )



    return render(request, 'formations/training_course.html', {'training_courses' : user.course.all()})