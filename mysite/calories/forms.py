from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    repeated_password = forms.CharField(label='password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    def check_password_match(self):
        cd = self.cleaned_data
        if cd['password'] != cd['repeated_password']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password']