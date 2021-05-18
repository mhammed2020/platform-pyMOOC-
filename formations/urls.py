from django.urls import path 

from . import views 

urlpatterns = [
    path('', views.list_view , name ='list-path'),
    path('<int:id>/', views.training_course , name ='training-path')

]
