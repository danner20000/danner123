from django.shortcuts import render
from .serializers import FileSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from django.utils import timezone
from datetime import timedelta
from django.contrib import messages
import requests

#import from form
from .forms import create_file
# Create your views here.
class File_Document(ModelViewSet):
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
def create_new_file(request):
    if request.method == 'POST':
        form1 = create_file(request.POST) 
        if form1.is_valid():
            select_BU = form1.cleaned_data['select_BU']
            document_type = form1.cleaned_data['document_type']
            department = form1.cleaned_data['department']
            upload_file = form1.cleaned_data['upload_file']
            renewal_date = form1.cleaned_data['renewal_date']
            expiry_date = form1.cleaned_data['expiry_date']

            user_data = {
                'select_BU': select_BU,
                'document_type': document_type,
                'department': department,
                'upload_file': upload_file,
                'renewal_date': renewal_date,
                'expiry_date': expiry_date
            }
            response = requests.post('http://127.0.0.1:8000/api/file/', data=user_data)

            if response.status_code == 201: 
                messages.success(request, 'User Created successful!')
                return render(request, 'create_new_file_form.html')
            else:
                messages.error(request, f'Error creating user: {response.status_code}')
        else:
            messages.error(request, 'Invalid forms. Please check your inputs.')
    else:
        form1 = create_file()
    return render(request, 'create_user_form.html', {'form': form1})


#all pages
#display valid file pages
def valid_file_list(request):
    return render(request, 'valid_file_list.html')

#display expired file pages
def expired_file_list(request):
    return render(request, 'expired_file_list.html')

#display expired file pages
def to_be_renew_file_list(request):
    return render(request, 'to_be_renew_file_list.html')

#display create new file pages
def create_new_file_form(request):
    return render(request, 'create_new_file_form.html')