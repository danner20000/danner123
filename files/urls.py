from django.urls import path,include
from . import views
from .views import (
    File_Document_view
)

urlpatterns = [
    path('',include([
        path('', File_Document_view.as_view({
            'get': 'list',
            'post': 'create',
        })),
        path('<int:pk>/', File_Document_view.as_view({
            'put': 'update',
            'delete': 'destroy',
        })),
        path('expired/', File_Document_view.as_view({
            'get': 'expired',  # Custom action for expired files
        })),
        path('valid_file/', File_Document_view.as_view({
            'get': 'valid_file',  # Custom action for valid files
        })),
        path('to_be_renew/', File_Document_view.as_view({
            'get': 'to_be_renew',  # Custom action for files to be renewed
        })),  
    ])),
    #create new file page
    path('create_new_file_form/', views.create_new_file_form, name='create_new_file_form'),
    #renew file page
    path('renew_file_form/<int:file_id>/', views.renew_file_form, name='renew_file_form'),

    #api
    #create new file api
    path('create_new_file/', views.create_new_file, name='create_new_file'),

    #get renew file list
    path('get_renew_file_list/', views.get_renew_file_list, name='get_renew_file_list'),
    #get expired file list
    path('get_expired_file_list/', views.get_expired_file_list, name='get_expired_file_list'),
    #get valid file list
    path('get_valid_file_list/', views.get_valid_file_list, name='get_valid_file_list'),
    #renew file api
    path('renew_file/<int:file_id>/', views.renew_file, name='renew_file'),
]