from django import forms
from django.core.exceptions import ValidationError
from users.models import User
import re

class RegisterUserForm(forms.ModelForm):
    confirm_password = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    class Meta:
        model = User
        fields = (
            'name',
            'email',
            'role',
            'country',
            'nationality',
            'mobile',
            'password',
            'confirm_password'
        )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-select'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'nationality': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
    
    def clean_name(self):
        name=self.cleaned_data.get('name')
        if not name:
            raise ValidationError("Name cannot be empty")
        if len(name) < 2:
            raise ValidationError("Name must be at least 2 characters long")
        return name

    def clean_mobile(self):
        mobile=self.cleaned_data.get('mobile')
        pattern = re.compile(r'^\d{10}$')
        if not re.match(pattern, mobile):
            raise ValidationError("Invalid mobile number. Please enter a 10-digit number.")
        return mobile
        
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        return cleaned_data    

class LoginUserForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
