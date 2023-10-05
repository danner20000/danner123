from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer
from django.contrib import messages
import requests
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404
from .models import User
from rest_framework import status
from django.core.paginator import Paginator
from .pagination import CustomPageNumberPagination


#import from form
from .forms import create_user_form
from .forms import login 
from .forms import update_user_form


# Create your views here.
class Users(ModelViewSet):
    serializer_class = UserSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    

#all function

#create user function -----------------------------------------------------------------------------
def create_user(request):
    if request.method == 'POST':
        form = create_user_form(request.POST) 
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            if password != confirm_password:
                messages.error(request, 'Passwords do not match. Please try again.')
                return render(request, 'create_user_form.html', {'form': form})

            user_data = {
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'password': password
            }
            response = requests.post('http://127.0.0.1:8000/api/users/', data=user_data)

            if response.status_code == 201: 
                messages.success(request, 'User Created successful!')
                return redirect('user_list') 
            else:
                messages.error(request, f'Error creating user: {response.status_code}')
        else:
            messages.error(request, 'Invalid forms. Please check your inputs.')
    else:
        form = create_user_form()
    return render(request, 'create_user_form.html', {'form': form})

#update user data -----------------------------------------------------------------------------
def update_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = update_user_form(request.POST)
        if form.is_valid():
            # Update user information here
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('user_list') 
    else:
        form = update_user_form(initial={
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
        })
    context = {'user': user, 'form': form}
    return render(request, 'update_user.html', context)

#handle login form submission. ---------------------------------------------------------------------
def login_form(request):
    if request.method == 'POST':
        form = login(request.POST) 
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful!')
                return redirect('dashboard') 
            else:
                messages.error(request, 'Invalid credentials. Please try again.')
    else:
        form = login()
    return render(request, 'login.html', {'form': form})
    


#all pages--------------------------------------------------------------------------------------------

#redirect to login
def redirect_to_login(request):
    return redirect('login_form')

#login page ----------------------------------------------------------------------------------------
def home(request):
    form = login() 
    return render(request, 'login.html', {'form': form})

#dashboard page --------------------------------------------------------------------------------
def dashboard(request):
    return render(request, 'dashboard.html')

#create user page -----------------------------------------------------------------------------
def create_user_page(request):
    form = create_user_form() 
    return render(request, 'create_user_form.html' , {'form': form})

#display user list page -----------------------------------------------------------------------
def user_list(request):
    users = User.objects.all()
    context = {"users": users}
    return render(request, 'user_list.html', context)

#display update user page -----------------------------------------------------------------------
def update_user_page(request, user_id):
    user = get_object_or_404(User, id=user_id)
    form = update_user_form(initial={
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
    })

    context = {'form': form}
    return render(request, 'update_user.html', context)





