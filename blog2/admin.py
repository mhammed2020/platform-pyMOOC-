from django.contrib import admin

# Register your models here.

from . models import Course



class CourseAdmin(admin.ModelAdmin) :
    list_display = ('title','author','post_date','duree', 'is_new')
    # list_diplay_links = ('title','duree')
    list_filter = ("post_date", )
admin.site.register(Course,CourseAdmin)