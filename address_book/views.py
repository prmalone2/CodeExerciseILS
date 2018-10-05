from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django import forms
from address_book.models import User

class NewUserForm(forms.Form):
    name = forms.CharField(label='Name')
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password')

class NewContactForm(forms.Form):
    firstName = forms.CharField(label='First Name')
    lastName = forms.CharField(label='Last Name')
    phoneNumber = forms.CharField(label='Phone Number')
    email = forms.CharField(label='Email Address')
    address = forms.CharField(label='Street Address')

class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password')

def index(request):
    template = loader.get_template('address_book/index.html')
    context = {}
    return HttpResponse(template.render(context, request))
    #return HttpResponse("Hello world, welcome to the address_book index")

def login(request):
    template = loader.get_template('address_book/login.html')
    form = LoginForm()
    context = {'form': form}
    response = HttpResponse(template.render(context, request))
    return response
    #return HttpResponse("This is where you login")

def new_user(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.isValid():
            n_user = User(form.cleaned_data['name'], form.cleaned_data['username'], form.cleaned_data['password'])
            n_user.save()
    form = NewUserForm()
    template = loader.get_template('address_book/new_user.html')
    context = {'form': form}
    return HttpResponse(template.render(context, request))
    #return HttpResponse("This is where you create a new user")

def user_page(request, username):
    return HttpResponse("This is where contacts for %s are displayed" % username)

def contact_display(request, username, contact_name):
    return HttpResponse("This is where information for %s is displayed for user %s" % (contact_name, username))
