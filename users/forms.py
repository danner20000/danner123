from django import forms

#login form
class login(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

#create user form
class create_user_form(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match. Please try again.")

        return cleaned_data
    
class update_user_form(forms.Form):
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    password = forms.CharField(widget=forms.PasswordInput)

