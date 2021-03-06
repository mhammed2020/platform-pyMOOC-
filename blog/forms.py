from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import  User
from django  import forms
from . models import Profile

class UserRegister(UserCreationForm) :
    class Meta :
        model = User
        fields = ('username','email')

class LoginForm(forms.ModelForm) :

    password = forms.CharField(widget =forms.PasswordInput())

    class Meta :
        model =User
        fields =('username', 'password')


class ProfileForm(forms.ModelForm) :
    class Meta :
        model = Profile
        fields = ('img',)

class ProfileFormUser(forms.ModelForm) :
    class Meta :
        model = User
        fields = ('username','email','first_name','last_name')
        
