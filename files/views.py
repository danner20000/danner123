from django.shortcuts import render ,redirect
from .serializers import FileSerializer , DepartmentSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from django.utils import timezone
from datetime import timedelta
from .models import File_Document ,Department
from django.shortcuts import render, get_object_or_404
import requests
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages

#import from form
from .forms import create_file
from .forms import renew_form

# Create your views here.
class Department_view(ModelViewSet):
    serializer_class = DepartmentSerializer

    def get_queryset(self):
        user_company = self.request.user.company
        return Department.objects.filter(company=user_company)


    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class File_Document_view(ModelViewSet):
    serializer_class = FileSerializer

    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
#get the expired file
 
    @action(detail=False, methods=['get'])
    def expired(self, request):
        queryset = self.get_queryset().filter(expiry_date__lt=timezone.now())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
#get the valid file
    @action(detail=False, methods=['get'])
    def valid_file(self, request):
        expiration_threshold = timezone.now() + timedelta(days=60)
        queryset = self.get_queryset().filter(
            expiry_date__gte=expiration_threshold
        )

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
#get the file to be renew
    @action(detail=False, methods=['get'])
    def to_be_renew(self, request):
        two_months_before_expiry = timezone.now() + timedelta(days=60)
        queryset = self.get_queryset().filter(expiry_date__gte=timezone.now(), expiry_date__lte=two_months_before_expiry)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
#create new file 
@login_required
def create_new_file(request):
    if request.method == 'POST':
        form = create_file(request.user.company, request.POST, request.FILES)
        if form.is_valid():
            department_name = form.cleaned_data['department_name']
            department = Department.objects.get(department_name=department_name)

            file_document = File_Document(
                user=request.user,
                company=request.user.company,
                department_name=department,  # Assign the Department instance, not the name
                document_type=form.cleaned_data['document_type'],
                upload_file=form.cleaned_data['upload_file'],
                renewal_date=form.cleaned_data['renewal_date'],
                expiry_date=form.cleaned_data['expiry_date']
            )
            file_document.save()

            messages.success(request, 'File created successfully!')
            return redirect('create_new_file_form')
        else:
            messages.error(request, 'Error creating file. Please check your inputs.')
    else:
        form = create_file(company=request.user.company)
    return render(request, 'create_new_file_form.html', {'form': form})


#renew the file 
@login_required
def renew_file(request, file_id):
    file = get_object_or_404(File_Document, id=file_id)
    if request.method == 'POST':
        form = renew_form(request.user.company, request.POST, request.FILES)
        if form.is_valid():
            department_name = form.cleaned_data['department_name']
            department = Department.objects.get(department_name=department_name)

            file.document_type = form.cleaned_data['document_type']
            file.department_name = department  # Assign the Department instance, not the name
            file.upload_file = form.cleaned_data['upload_file']
            file.renewal_date = form.cleaned_data['renewal_date']
            file.expiry_date = form.cleaned_data['expiry_date']
            file.save()

            messages.success(request, 'File renewed successfully!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Error renewing file. Please check your inputs.')
            print(f'Form Errors: {form.errors}')
    else:
        form = renew_form(request.user.company, initial={ 
            'document_type': file.document_type,
            'department_name': file.department_name.department_name,  # Provide the department name
        })

    context = {'form': form, 'file': file}
    return render(request, 'renew_file_form.html', context)



#all pages
#get expired file list
def get_expired_file_list(request):
    response = requests.get('http://127.0.0.1:8000/api/file/expired/')
    if response.status_code == 200:
        expired_file = response.json()
        paginator = Paginator(expired_file, 5)
        page_number = request.GET.get('page')
        expired_file = paginator.get_page(page_number)
        return render(request, 'expired_file_list.html', {'expired_file': expired_file})
    else:
        return render(request, 'error_page.html')

#get expired file list
def get_valid_file_list(request):
    response = requests.get('http://127.0.0.1:8000/api/file/valid_file/')
    if response.status_code == 200:
        valid_file = response.json()
        paginator = Paginator(valid_file, 5)
        page_number = request.GET.get('page')
        valid_file = paginator.get_page(page_number)

        return render(request, 'valid_file_list.html', {'valid_file': valid_file})
    else:
        return render(request, 'error_page.html')


#get expired file list
def get_renew_file_list(request):
    response = requests.get('http://127.0.0.1:8000/api/file/to_be_renew/')
    if response.status_code == 200:
        renew_file = response.json()
        paginator = Paginator(renew_file, 5)
        page_number = request.GET.get('page')
        renew_file = paginator.get_page(page_number)
        return render(request, 'to_be_renew_file_list.html', {'renew_file': renew_file})
    else:
        return render(request, 'error_page.html')

#display create new file pages
@login_required
def create_new_file_form(request):
    context = {'form': create_file(request.user.company)}
    return render(request, 'create_new_file_form.html', context)


#display renew file pages
@login_required
def renew_file_form(request, file_id):
    file = get_object_or_404(File_Document, id=file_id)
    form = renew_form(company=request.user.company, initial={
        'document_type': file.document_type,
        'department': file.department_name,
    }) 
    context = {'form': form, 'file': file}
    return render(request, 'renew_file_form.html', context)


