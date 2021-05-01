from django.urls import path

from . import views 
urlpatterns = [
    path('', views.post_list, name ="home-post-path"),
    path('course/<int:id>/', views.detail, name ="detail-path"),
    path('create/', views.create_course, name ="create-path"),
    path('update/<int:id>/', views.update_course, name ="update-path"),
    path('delete/<int:id>', views.delete_course, name ="delete-path")


]
