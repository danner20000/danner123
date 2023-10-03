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
    ])),
]