from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from mainapp.models import UserProfile,Posts,Comments

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']


class SignInForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

class UserProfileModelForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=['full_name','profile_picture','bio','phone']
        # 'following','followers']


class CreatePostModelForm(forms.ModelForm):
    class Meta:
        model=Posts
        fields=['title','post_image','post_video']
        # ['title','post_image','post_video']


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields=['text']

