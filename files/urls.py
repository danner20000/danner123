from django.urls import path,include
from . import views

from .views import (
    Files
)

urlpatterns = [
    path('',include([
        path('', Files.as_view({
            'get': 'list',
            'post': 'create',
        })),
        path('<int:pk>/', Files.as_view({
            'put': 'update',
            'delete': 'destroy',
        })),
        path('expired/', Files.as_view({
            'get': 'expired',  # Custom action for expired files
        })),
        path('valid_file/', Files.as_view({
            'get': 'valid_file',  # Custom action for valid files
        })),
        path('to_be_renew/', Files.as_view({
            'get': 'to_be_renew',  # Custom action for files to be renewed
        })),
    ])),
]