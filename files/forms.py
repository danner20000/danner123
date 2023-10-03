from django import forms
from .models import Files

class create_file(forms.Form):
    class Meta:
        model = Files
        fields = ['select_BU', 'document_type', 'department', 'upload_file', 'renewal_date', 'expiry_date']
