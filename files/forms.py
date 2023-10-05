from django import forms

class create_file(forms.Form):
    select_BU = forms.ChoiceField(
        choices=[
            ('Select Company','- Select Company -'),
            ('fishing company', 'Fishing Company'),
            ('holy child', 'Holy Child'),
            ('sto. niño', 'Sto. Niño'),
        ],
        initial='Select Company',
        required=True,
        widget=forms.Select(attrs={'style': 'width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box;'})
    )
    document_type = forms.ChoiceField(
        choices=[
             ('Select Document Type', '- Select Document Type -'),
            ('contract', 'Contract'),
            ('invoice', 'Invoice'),
            ('report', 'Report'),
        ],
        initial='Select Document Type',
        required=True,
        widget=forms.Select(attrs={'style': 'width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box;'})
    )
    department = forms.ChoiceField(
        choices=[
            ('Select Department', '- Select Department -'),
            ('department of health', 'Department of Health'),
            ('human resource', 'Human Resource'),
            ('registrar', 'Registrar'),
        ],
        initial='Select Department',
        required=True,
        widget=forms.Select(attrs={'style': 'width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box;'})
    )
    upload_file = forms.FileField()
    renewal_date = forms.DateField(
        required=True,
        widget=forms.TextInput(attrs={'type': 'date', 'style': 'display: inline-block; width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box;'})
    )

    expiry_date = forms.DateField(
        required=True,
        widget=forms.TextInput(attrs={'type': 'date', 'style': 'display: inline-block; width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box;'})
    )



class renew_file(forms.Form):
    select_BU = forms.ChoiceField(
        choices=[
            ('Select Company','- Select Company -'),
            ('fishing company', 'Fishing Company'),
            ('holy child', 'Holy Child'),
            ('sto. niño', 'Sto. Niño'),
        ],
        initial='Select Company',
        required=True,
        widget=forms.Select(attrs={'style': 'width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box;'})
    )
    document_type = forms.ChoiceField(
        choices=[
             ('Select Document Type', '- Select Document Type -'),
            ('contract', 'Contract'),
            ('invoice', 'Invoice'),
            ('report', 'Report'),
        ],
        initial='Select Document Type',
        required=True,
        widget=forms.Select(attrs={'style': 'width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box;'})
    )
    department = forms.ChoiceField(
        choices=[
            ('Select Department', '- Select Department -'),
            ('department of health', 'Department of Health'),
            ('human resource', 'Human Resource'),
            ('registrar', 'Registrar'),
        ],
        initial='Select Department',
        required=True,
        widget=forms.Select(attrs={'style': 'width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box;'})
    )
    upload_file = forms.FileField()
    renewal_date = forms.DateField(
        required=True,
        widget=forms.TextInput(attrs={'type': 'date', 'style': 'display: inline-block; width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box;'})
    )

    expiry_date = forms.DateField(
        required=True,
        widget=forms.TextInput(attrs={'type': 'date', 'style': 'display: inline-block; width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box;'})
    )




