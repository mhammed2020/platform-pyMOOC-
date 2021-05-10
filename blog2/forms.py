from django import forms 
from . models import Course
from ckeditor.widgets import CKEditorWidget
class CourseForm(forms.ModelForm) :    
    
    content = forms.CharField(widget=CKEditorWidget())
    class Meta :
        model = Course
        fields = "__all__"
        exclude = ('author',)
        