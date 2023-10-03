from rest_framework import serializers
from files.models import Files

class FileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    class Meta:
        model = Files
        fields = (
            'user',
            'select_BU',
            'document_type',
            'department',
            'upload_file',
            ' renewal_date',
            'expiry_date',
        )