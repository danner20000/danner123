"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from users.views import redirect_to_login, login_form,dashboard, create_user, create_user_page, user_list, update_user, update_user_page
from files.views import valid_file_list ,expired_file_list ,to_be_renew_file_list, create_new_file_form,create_new_file, renew_file_form
urlpatterns = [
    path('admin/', admin.site.urls),
     path('api/', include([
        path('users/', include('users.urls')),
        path('file/', include('files.urls')),
    ])),

    #pages
    #Redirect Login
    path('', redirect_to_login),
    #Display dashboard
    path('dashboard/', dashboard, name='dashboard'),
    #Display create user page
    path('create_user_page/', create_user_page, name='create_user_page'),
    #Display user list page
    path('user_list/', user_list, name='user_list'),
    #Display update user page
    path('update_user_page/', update_user_page, name='update_user_page'),
    #Display valid file page
    path('valid_file_list/', valid_file_list, name='valid_file_list'),
    #Display expired file page
    path('expired_file_list/', expired_file_list, name='expired_file_list'),
    #Display to be renew file page
    path('to_be_renew_file_list/', to_be_renew_file_list, name='to_be_renew_file_list'),
    #Create new file page
    path('create_new_file_form/', create_new_file_form, name='create_new_file_form'),
    #renew file page
    path('renew_file_form/', renew_file_form, name='renew_file_form'),



    #functions
    #user
    #login function
    path('login/', login_form, name='login_form'),
    #create user api function
    path('create_user/', create_user, name='create_user'),
    
    #file
     #create file api function
    path('create_new_file/', create_new_file, name='create_new_file'),
    #update user api
    path('update_user/', update_user, name='update_user'),
]
