from django.contrib import admin

# Register your models here.

from . models import Course


class CourseAdmin(admin.ModelAdmin) :
    list_display = ('title','author', 'post_date','price','is_new')
   #list_display_links = None 
   #list_editable = ('post_date','price','author','is_new')
    list_filter = ("author",'post_date' )
  
    #Search Feature
    search_fields = ['title']
    fields =['title','author']
  
admin.site.register(Course,CourseAdmin)