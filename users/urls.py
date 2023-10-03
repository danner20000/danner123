from django.urls import path,include
from . import views

from .views import (
    Users
)

urlpatterns = [
    path('',include([
        path('', Users.as_view({
            'get': 'list',
            'post': 'create',
        })),
        path('<int:pk>/', Users.as_view({
            'put': 'update',
            'delete': 'destroy',
        })),
      
    ])),
    path('users/<int:pk>/', Users.as_view({'delete': 'destroy'}), name='users-detail'),

    #api
    #create user
    path('create_user/', views.create_user, name='create_user'),
   

    #pages
    #dashboard page
    path('dashboard/', views.dashboard, name='dashboard'),
    #create user page
    path('create_user_page/', views.create_user_page, name='create_user_page'),
    #create user list page
    path('user_list/', views.user_list, name='user_list'),
    #create update user page
    path('update_user/<int:user_id>/', views.update_user, name='update_user'),

]