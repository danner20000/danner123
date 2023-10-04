from django.shortcuts import render ,redirect
from .serializers import FileSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from django.utils import timezone
from datetime import timedelta
from django.contrib import messages
import requests
from .models import File_Document


#import from form
from .forms import create_file

# Create your views here.
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
def create_new_file(request):
    if request.method == 'POST':
        form = create_file(request.POST, request.FILES)
        if form.is_valid():
            # Assuming 'form' contains cleaned data including all fields
            file_document = File_Document(
                user=request.user,
                select_BU=form.cleaned_data['select_BU'],
                document_type=form.cleaned_data['document_type'],
                department=form.cleaned_data['department'],
                upload_file=form.cleaned_data['upload_file'],
                renewal_date=form.cleaned_data['renewal_date'],
                expiry_date=form.cleaned_data['expiry_date']
            )
            file_document.save()

            return redirect('create_new_file_form')

    else:
        form = create_file()
    return render(request, 'create_new_file_form.html', {'form': form})




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
    context = {'form': create_file}
    return render(request, 'create_new_file_form.html',context)