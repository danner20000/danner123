from django.urls import path,include

from .views import (
    File_Document
)

urlpatterns = [
    '''path('',include([
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
    ])),'''
]