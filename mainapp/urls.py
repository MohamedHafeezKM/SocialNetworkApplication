from django.urls import path,include

from mainapp import views

urlpatterns = [
   
    path('register/',views.RegisterView.as_view(),name='register'),
    path('profile/',views.ProfileView.as_view(),name='profile'),
    path('signin/',views.SignInView.as_view(),name='signin'),
    path('createprofile/',views.ProfileCreateView.as_view(),name='profile_create'),
    path('',views.HomeView.as_view(),name='home'),
    path('updateprofile/<int:pk>',views.ProfileUpdateView.as_view(),name='profile_update'),
    path('all_users/',views.AllUserProfileView.as_view(),name='all_users'),
    path('follow/<int:pk>',views.FollowView.as_view(),name='follow'),
    path('logout/',views.SignOutView.as_view(),name='signout'),
    path('posts/<int:pk>/remove',views.PostDeleteView.as_view(),name='remove_post'),
    path('posts/<int:pk>/like',views.LikeView.as_view(),name='like_post'),
    path('posts/comment',views.AddCommentView.as_view(),name='comment_post'),
    

]
