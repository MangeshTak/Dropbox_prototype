from django import forms
from django.contrib.auth.models import User
from Box.models import *


class Loginform(forms.Form):
    username=forms.CharField(max_length=50)
    password=forms.CharField(widget=forms.PasswordInput)

class UserRegistration(forms.ModelForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Repeat Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model=User
        fields= ('username','first_name','email')
        widgets = {
            'username':forms.TextInput(attrs={'class':'input'}),
            'first_name': forms.TextInput(attrs={'class': 'input'}),
            'email': forms.EmailInput(attrs={'class': 'input'}),

        }


    def clean_password2(self):
        cd=self.cleaned_data
        if cd['password']!=cd['password2']:
            raise forms.ValidationError('Passwords do not match')
        return cd['password2']

class Fileupload(forms.ModelForm):
    class Meta:
        model= user_files
        fields = ('Filename','Browse')

class Share_file(forms.ModelForm):
    class Meta:
        model = share_files
        fields = ('select_file', 'select_user')

class delete_file(forms.ModelForm):
    class Meta:
        model = user_files
        fields = ('Filename',)



