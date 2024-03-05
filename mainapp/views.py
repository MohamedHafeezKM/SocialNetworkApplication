from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import CreateView,TemplateView,FormView,ListView,UpdateView,View
from django.urls import reverse_lazy
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator

# Create your views here.
from mainapp.forms import RegisterForm,SignInForm,CreatePostModelForm,UserProfileModelForm,CreateCommentForm
from mainapp.models import Posts,UserProfile,Comments
from mainapp.decorators import rule


class RegisterView(CreateView):
    template_name='user/register.html'
    form_class=RegisterForm
    success_url=reverse_lazy('signin')

@method_decorator(rule,name='dispatch')
class ProfileView(ListView):
    template_name='user/profile.html'
    form_class=CreatePostModelForm
    success_url=reverse_lazy('home')
    model=Posts
    context_object_name='my_post'

    def get_queryset(self):
        qs=Posts.objects.filter(user=self.request.user).order_by('-id')
        return qs
    
    

@method_decorator(rule,name='dispatch')
class ProfileCreateView(CreateView):
    template_name='user/createprofile.html'
    form_class=UserProfileModelForm
    success_url=reverse_lazy('profile')
    context_object_name='form'

    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    
@method_decorator(rule,name='dispatch')    
class ProfileUpdateView(UpdateView):
    template_name='user/updateprofile.html'
    form_class=UserProfileModelForm
    success_url=reverse_lazy('profile')
    model=UserProfile

    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)


class SignInView(FormView):
    template_name='user/signin.html'
    form_class=SignInForm

    def post(self,request,*args,**kwargs):
        user_name=request.POST.get('username')
        pass_word=request.POST.get('password')
        user_object=authenticate(request,username=user_name,password=pass_word)
        if user_object:
            login(request,user_object)
            messages.success(request,'Logged in')
            return redirect('profile')
        messages.error(request,'Failed')
        return render(request,self.template_name)
        
@method_decorator(rule,name='dispatch')
class HomeView(CreateView,ListView):
    template_name='user/home.html'
    form_class=CreatePostModelForm
    success_url=reverse_lazy('home')
    model=Posts
    context_object_name='all_post'

    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    
    def get_queryset(self):
        qs=Posts.objects.filter(user__in=self.request.user.profile.following.all()).order_by('-id')
        return qs
    

@method_decorator(rule,name='dispatch')
class AllUserProfileView(ListView):
    template_name='user/all_users.html'
    context_object_name='all_users'
    model=UserProfile

    def post(self,request,*args,**kwargs):
        name=request.POST.get('box')
        qs=UserProfile.objects.filter(full_name__icontains=name)
        return render(request,'user/all_users.html',{'qs':qs})


@method_decorator(rule,name='dispatch')
class FollowView(View):
    def post(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        usertofollow=User.objects.get(id=id)
        action=request.POST.get('action')
        if action=='follow':
            request.user.profile.following.add(usertofollow)
            usertofollow.profile.followers.add(request.user)
            messages.success(request,'Successfully following')

        elif action=='unfollow':
            request.user.profile.following.remove(usertofollow)
            usertofollow.profile.followers.remove(request.user)
            messages.success(request,'Unfollowed!')
        return redirect('all_users')

@method_decorator(rule,name='dispatch')
class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect('signin')
    
@method_decorator(rule,name='dispatch')
class PostDeleteView(View):
    def post(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        post=Posts.objects.get(id=id)
        if post.user==request.user:
            post.delete()
        else:
            messages.error(request,'Permission denined!')

        return redirect('profile')
    
@method_decorator(rule,name='dispatch')
class LikeView(View):
    def post(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        action=request.POST.get('action')
        if action=='like':
            Posts.objects.get(id=id).liked_by.add(request.user)
        elif action=='unlike':
            Posts.objects.get(id=id).liked_by.remove(request.user)
            
        return redirect('home')
    
@method_decorator(rule,name='dispatch')
class AddCommentView(CreateView):
    template_name='user/home.html'
    form_class=CreateCommentForm
    success_url=reverse_lazy('home')
   

    

    def form_valid(self, form):
        form.instance.user=self.request.user
        post_id=self.request.POST.get('post_id')
        post=Posts.objects.get(id=post_id)
        form.instance.post=post
        return super().form_valid(form)
    
    

    
