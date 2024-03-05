from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    full_name=models.CharField(max_length=20,null=True)
    profile_picture=models.ImageField(upload_to='profilepics',null=True,blank=True)
    bio=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=10,null=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile',null=True)
    followers=models.ManyToManyField(User,related_name='follower')
    following=models.ManyToManyField(User,related_name='me_following')

    def __str__(self) -> str:
        return self.user
 
    
class Posts(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=200,null=True)
    post_image=models.ImageField(upload_to='imagepost',null=True,blank=True)
    post_video=models.FileField(upload_to='video_post',null=True,blank=True)
    created_date=models.DateTimeField(auto_now_add=True,null=True)
    liked_by=models.ManyToManyField(User,related_name='liked')

    def __str__(self) -> str:
        return self.title

class Comments(models.Model):
    text=models.CharField(max_length=200)
    post=models.ForeignKey(Posts,on_delete=models.CASCADE,null=True,related_name='comment')
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING,null=True)
    created_date=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self) -> str:
        return self.text
    
class Stories(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    story_image=models.ImageField(upload_to='imagestory',null=True,blank=True)
    story_video=models.FileField(upload_to='videostory',null=True,blank=True)
    created_date=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self) -> str:
        return self.title




