from django import forms

from .models import Company

#create user form
class create_user_form(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
       
    }))
    company = forms.ModelChoiceField(
        queryset=Company.objects.all(),
        empty_label="Select a Company",
        widget=forms.Select(attrs={
            'class': 'form-control',
            
        })
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
      
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
      
    }))

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match. Please try again.")

        return cleaned_data


class update_user_form(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
       
         
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
       
    }))
    company = forms.CharField(widget=forms.TextInput(attrs={
        
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        
    }))


class company_form(forms.ModelForm):
    
    company_name = forms.CharField(
        widget=forms.TextInput(attrs={'style': 'background-color: #f7f7f7; padding: 5px;'})
    )
    class Meta:
        model = Company
        fields = ['company_name']