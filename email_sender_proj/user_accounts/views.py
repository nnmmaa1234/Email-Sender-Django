from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
#def RegisterPage(request):
#    form = UserCreationForm()
#
#    if request.method == 'POST':
#        form = UserCreationForm(request.POST)
#        if form.is_valid():
#            form.save()
#
#    context = {'form':form}
#    return render(request, 'Registeration/registeration.html',context)

def RegisterPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            #login(request, user)
            
            messages.success(request, f'Account was created for {user}')
            
            subject = 'welcome to this site'
            message = 'Hi, thank you for registering'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ]
            send_mail( subject, message, email_from, recipient_list )
            login(request, user)
            
            #return redirect('/landing/')

    context = {'form':form}
    return render(request, 'user_accounts/registeration.html',context)

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('/landing/')

    context = {}
    return render(request, 'user_accounts/login.html',context)