from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer
from django.contrib import messages
import requests
from django.contrib.auth import authenticate, login, logout

#import from form
from .forms import create_user_form
from .forms import login


# Create your views here.
class User(ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
#all function

#create user function
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
                return render(request, 'user_list.html')
            else:
                messages.error(request, f'Error creating user: {response.status_code}')
        else:
            messages.error(request, 'Invalid forms. Please check your inputs.')
    else:
        form = create_user_form()
    return render(request, 'create_user_form.html', {'form': form})


#handle login form submission.
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

#all pages

#redirect to login
def redirect_to_login(request):
    return redirect('login_form')

#login page
def home(request):
    form = login() 
    return render(request, 'login.html', {'form': form})

#dashboard page
def dashboard(request):
    return render(request, 'dashboard.html')

#create user page
def create_user_page(request):
    form = create_user_form() 
    return render(request, 'create_user_form.html' , {'form': form})

#display user list page
def user_list(request):
    return render(request, 'user_list.html')