from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import User, BLOOD_GROUPS, SEX
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate, login



# Custom widget
class DateInput(forms.DateInput):
    input_type = 'date'


class LoginForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'name': 'username',
            'id': 'validationCustom08'
        }
    ))

    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'name': 'password',
            'id': 'validationCustom09'
        }
    ))

    class Meta:
        model = User
        fields = ('username', 'password')

    def clean(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']

            if not authenticate(username=username, password=password):
                raise forms.ValidationError('Email and password did not match any user in our database')


class UserRegistrationForm(forms.ModelForm):

    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'name': 'first_name',
        }
    ))

    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'name': 'last_name',
        }
    ))

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'name': 'email',
        }
    ))

    address = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'name': 'address',
        }
    ))

    date_of_birth = forms.DateField(widget=DateInput)

    blood_group = forms.ChoiceField(choices=BLOOD_GROUPS, widget=forms.Select(
        attrs={
            'class': 'form-control',
        }
    ))

    sex = forms.ChoiceField(choices=SEX, widget=forms.Select(
        attrs={
            'class': 'form-control',
        }
    ))
    
    mobile_number = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'name': 'contact_number',
        }
    ))

    pic = forms.ImageField(widget=forms.FileInput(
        attrs={
            'id':"file",
            'class': 'form-control image-input',
        }
    ))

    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'name': 'password',
            'minlength': "8",
        }
    ))
    password2 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'name': 'password',
            'minlength': "8",
        }
    ))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'address', 'date_of_birth', 'mobile_number', 'blood_group', 'sex', 'pic', )

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords dont match')


class UserUpdateForm(forms.ModelForm):

    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'name': 'first_name',
            'placeholder': "Enter First Name"
        }
    ))

    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'name': 'last_name',
            'placeholder': "Enter Last Name"
        }
    ))

    address = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'name': 'address',
            'placeholder': "Address"
        }
    ))
    
    mobile_number = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'name': 'contact_number',
            'placeholder': "Enter Mobile Number"
        }
    ))

    pic = forms.ImageField(widget=forms.FileInput(
        attrs={
            'id':"file",
            'class': 'form-control image-input',
        }
    ))


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'address', 'mobile_number', 'pic', )

class MyPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["old_password"].widget = forms.PasswordInput(attrs={"class": "form-control"})
        self.fields["new_password1"].widget = forms.PasswordInput(attrs={"class": "form-control"})
        self.fields["new_password2"].widget = forms.PasswordInput(attrs={"class": "form-control"})