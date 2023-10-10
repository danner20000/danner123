from rest_framework import serializers
from files.models import File_Document, Department

class FileSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source='user.email', read_only=True)
    company_name = serializers.EmailField(source='user.company', read_only=True)
    department_name = serializers.CharField(source='department_name.department_name', read_only=True)
    
    class Meta:
        model = File_Document
        fields = (
            'id',
            'user_email',
            'company_name',
            'department_name',
            'document_type',
            'upload_file',
            'renewal_date',
            'expiry_date',
        )

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = (
            'id',
            'company',
            'department_name',
        )