from django import forms

class create_file(forms.Form):
    select_BU = forms.ChoiceField(choices=[
            ('fishing company', 'Fishing Company'),
            ('holy child', 'Holy Child'),
            ('sto. niño', 'Sto. Niño'),
        ], initial='Select Company', required=True)
    document_type = forms.ChoiceField(choices=[
            ('contract', 'Contract'),
            ('invoice', 'Invoice'),
            ('report', 'Report'),
        ], initial='Select Document Type', required=True)
    department = forms.ChoiceField(choices=[
            ('department of health', 'Department of Health'),
            ('human resource', 'Human Resource'),
            ('registrar', 'Registrar'),
        ], initial='Select Department', required=True)
    upload_file = forms.FileField(required=True)
    renewal_date = forms.DateField(required=True, widget=forms.TextInput(attrs={'type': 'date'}))
    expiry_date = forms.DateField(required=True, widget=forms.TextInput(attrs={'type': 'date'}))