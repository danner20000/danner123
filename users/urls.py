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

    #api
    path('create_user/', views.create_user, name='create_user'),

    #pages
    #dashboard page
    path('dashboard/', views.dashboard, name='dashboard'),
    #create user page
    path('create_user_page/', views.create_user_page, name='create_user_page'),
]