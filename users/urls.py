from django.urls import path,include
from . import views

from .views import (
    User
)

urlpatterns = [
    path('',include([
        path('', User.as_view({
            'get': 'list',
            'post': 'create',
        })),
        path('<int:pk>/', User.as_view({
            'put': 'update',
            'delete': 'destroy',
        })),
    ])),
]