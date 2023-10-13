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
from users.views import dashboard, create_user, create_user_page, user_list, update_user, update_user_page ,redirect_to_login, login_user, login_page, logout_user,user_profile
from files.views import create_new_file_form,create_new_file, renew_file_form ,get_expired_file_list, get_renew_file_list,get_valid_file_list,renew_file ,display_admin_expired, display_admin_valid, display_admin_to_be_renew
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include([
        path('users/', include('users.urls')),
        path('file/', include('files.urls')),
    ])),

    #pages
    path('', redirect_to_login, name='root'),
    #Display login page
    path('login_page/', login_page, name='login_page'),
    #Display dashboard
    path('dashboard/', dashboard, name='dashboard'),
    #Display create user page
    path('create_user_page/', create_user_page, name='create_user_page'),
    #Display user list page
    path('user_list/', user_list, name='user_list'),
    #Display update user page
    path('update_user_page/', update_user_page, name='update_user_page'),
    #Create new file page
    path('create_new_file_form/', create_new_file_form, name='create_new_file_form'),
    #renew file page
    path('renew_file_form/', renew_file_form, name='renew_file_form'),
    #user profile
    path('user_profile/', user_profile, name='user_profile'),

    #render admin dashboard
    path('admin_expired/', display_admin_expired, name='admin_expired'),
    path('admin_valid/', display_admin_valid, name='admin_valid'),
    path('admin_to_be_renew/', display_admin_to_be_renew, name='admin_to_be_renew'),


    #functions
    #user
    #login user api function
    path('login_user/', login_user, name='login_user'),
    path('logout_user/', logout_user, name='logout_user'),
    #create user api function
    path('create_user/', create_user, name='create_user'),
    #update user api
    path('update_user/', update_user, name='update_user'),

    #file
    #create file api function
    path('create_new_file/', create_new_file, name='create_new_file'),
    
    #get expired list api
    path('get_expired_file_list/', get_expired_file_list, name='get_expired_file_list'),
    #get valid list api
    path('get_valid_file_list/', get_valid_file_list, name='get_valid_file_list'),
    #get renew list api
    path('get_renew_file_list/', get_renew_file_list, name='get_renew_file_list'),
    #renew document api
    path('renew_file/', renew_file, name='renew_file'),

]
