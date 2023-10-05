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
    #valid file page
    path('valid_file_list/', views.valid_file_list, name='valid_file_list'),
    #expired file page
    path('expired_file_list/', views.expired_file_list, name='expired_file_list'),
    #expired file page
    path('to_be_renew_file_list/', views.to_be_renew_file_list, name='to_be_renew_file_list'),
    #create new file page
    path('create_new_file_form/', views.create_new_file_form, name='create_new_file_form'),
    #renew file page
    path('renew_file_form/<int:file_id>/', views.renew_file_form, name='renew_file_form'),

    #api 
    #create new file api
    path('create_new_file/', views.create_new_file, name='create_new_file'),
]