from django.urls import path,include
from . import views
from .views import (
    File_Document
)

urlpatterns = [
    path('',include([
        path('', File_Document.as_view({
            'get': 'list',
            'post': 'create',
        })),
        path('<int:pk>/', File_Document.as_view({
            'put': 'update',
            'delete': 'destroy',
        })),
        path('expired/', File_Document.as_view({
            'get': 'expired',  # Custom action for expired files
        })),
        path('valid_file/', File_Document.as_view({
            'get': 'valid_file',  # Custom action for valid files
        })),
        path('to_be_renew/', File_Document.as_view({
            'get': 'to_be_renew',  # Custom action for files to be renewed
        })),  
    ])),
    #valid file page
    path('valid_file_list/', views.valid_file_list, name='valid_file_list'),
    #expired file page
    path('expired_file_list/', views.expired_file_list, name='expired_file_list'),
    #expired file page
    path('to_be_renew_file_list/', views.to_be_renew_file_list, name='to_be_renew_file_list'),
]