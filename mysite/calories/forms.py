from django import forms
from django.contrib.auth.models import User
from .models import EatenFood

class EatenFoodForm(forms.ModelForm):

    class Meta:
        model = EatenFood
        fields = ['food', 'weight_eaten', 'eating_time']
        widgets = {
            'eating_time': forms.DateTimeInput(attrs={'type':'datetime-local'}),
        }

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']