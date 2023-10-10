from rest_framework import serializers
from files.models import File_Document, Department

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File_Document
        fields = (
            'id',
            'user',
            'department',
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