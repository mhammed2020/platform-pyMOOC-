from django.urls import path 

from . import views 

urlpatterns = [
    path('', views.list_view , name ='list-path'),
    path('<str:slug>/', views.training_course , name ='training-path'),
    path('courses/<str:slug>/', views.coure_detail , name ='coure_detail-path'),
    
    
    


]
