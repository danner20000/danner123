from django import forms


#create user form
class create_user_form(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'style': 'width: 100%; padding: 8px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box;'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'style': 'width: 100%; padding: 8px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box;'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'style': 'width: 100%; padding: 8px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box;'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'style': 'width: 100%; padding: 8px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box;'
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'style': 'width: 100%; padding: 8px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box;'
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
        'style': 'width: 100%; padding: 8px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box;','readonly': 'readonly',
         
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'style': 'width: 100%; padding: 8px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box;',
        'readonly': 'readonly' 
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'style': 'width: 100%; padding: 8px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box;',
        'readonly': 'readonly' 
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'style': 'width: 100%; padding: 8px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box;'
    }))