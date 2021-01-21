"""goalpost URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from blog import views


admin.site.site_header = "Hi Lakshay!! Welcome to DailyRumble"
admin.site.site_title = "Welcome to DailyRumble "
admin.site.index_title = "Welcome to the Portal"

urlpatterns = [
       # Api to post a comment
    path('blogComment/',views.blogComment, name='blogComment'),
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path("blog/blogpost/<str:slug>/", views.blogpost, name='blogpost'),
    path('search/', views.search, name='search'),
    path('signup/', views.handleSignup, name='handleSignup'),
    path('user_login/', views.user_login, name='user_login'),
    path('logout/', views.handleLogout, name='handleLogout'),
 
    path('reset_password/', 
    auth_views.PasswordResetView.as_view(template_name="password_reset.html"), 
    name = "reset_password"),
 
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), name="password_reset_done"),
 
    path('reset/<uidb64>/<token>/', 
    auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),
     name="password_reset_confirm"),
 
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), name="password_reset_complete"),

]
