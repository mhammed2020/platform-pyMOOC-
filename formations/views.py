from django.shortcuts import redirect, render
from . models import Course, Training
# Create your views here.

def list_view(request) :
    
    return render(request,'formations/list_view.html',{'training' :Training.objects.all()})





def training_course(request,slug) :
    user = Training.objects.get(slug = slug )


    return render(request, 'formations/training_course.html', {'training_courses' : user.course.all()})

def coure_detail(request,slug) :
    #obj = Course.objects.get(slug=slug1)
    #print(obj.training.slug ,"***********************************")
    # return redirect('coure_detail-path' , slug = obj.slug)

    return render(request,'formations/course_detail.html',{'course' :Course.objects.get(slug=slug),
                                                           
                                                           'training' :Training.objects.all()
                                                           
                                                           })