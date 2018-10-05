from django import forms

class NewUserForm(forms.Form):
    name = forms.CharField(label='Name: ')
    username = forms.CharField(label='Username: ')
    password = forms.CharField(label='Password: ')

class NewContactForm(forms.Form):
    firstName = forms.CharField(label='First Name: ')
    lastName = forms.CharField(label='Last Name: ')
    phoneNumber = forms.CharField(label='Phone Number: ')
    email = forms.CharField(label='Email Address: ')
    address = forms.CharField(label='Street Address')

class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password')