from django.shortcuts import render,redirect
from . forms import CourseForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from . decorators import author_required
from django.core.exceptions import PermissionDenied

from . filters import CourseFilter
# Create your views here.
from . models import Course
def post_list(request) :

    # filters
    filter_obj= CourseFilter(request.GET) # fetch all data from data base ,, if request.GET={}==>
                                           # CourseFilter fetch all data

    #print(CourseFilter(request.GET).queryset,"-------------CourseFilter(request.GET).queryset -------------")
    #print(filter_obj.qs,"-------------filter_obj.qs------------------")

    course_list = filter_obj.qs
    paginator = Paginator(course_list, 6) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    #print(request.GET.get('page'),"*************request.GET.get('page')************")
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog2/post_list.html' ,  {'page_obj': page_obj ,
                                                      'filter_obj' : filter_obj } )



#pagination






def detail(request,id) :


    return render(request, 'blog2/detail.html' ,  {'post' :Course.objects.get(id=id) })

@login_required(login_url='login-path')
def create_course(request) :

    if request.method =='POST':
        obj = CourseForm(request.POST,request.FILES)

        if obj.is_valid() :

            obj = obj.save(commit=False)
            obj.author = request.user
            obj.save()

            # return f'/course/{obj.pk}/'
            #return reverse(f'course/{obj.pk}/')

            #return redirect('home-post-path')
            #slug = f'course/{obj.pk}/'
            #return redirect(slug)
            return redirect('detail-path' , id = obj.pk)

    return render(request, 'blog2/create.html' ,  {'form' :CourseForm()})




@login_required(login_url='login-path')
@author_required
def update_course(request,id) :

    # course = Course.objects.get(id=id)
    # if course.author == request.user  :

    if request.method == 'POST' :

        obj=CourseForm(request.POST, request.FILES, instance=Course.objects.get(id=id))
        if obj.is_valid() :
            obj = obj.save(commit=False)
            obj.author = request.user
            obj.save()
            return redirect('home-post-path')

    # else :
    #     raise  PermissionDenied #redirect('home-post-path')

    return render(request,'blog2/update.html', {'form' :
        CourseForm(instance=Course.objects.get(id=id)) ,
        'course' :Course.objects.get(id=id)
        })


@login_required(login_url='login-path')
@author_required
def delete_course(request,id) :
    obj=Course.objects.get(id=id)


    # if obj.author == request.user :
    if request.method =='POST' :
        obj.delete()
        return redirect('home-post-path')
    # else :
    #     return redirect('home-post-path')

    return render(request,'blog2/delete.html',{'course' :Course.objects.get(id=id)})


def user_course(request,username) :
    user = User.objects.get(username = username )



    return render(request, 'blog2/user_course.html', {'user_posts' : user.course.all()})
