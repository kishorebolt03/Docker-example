from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'users/index.html')

def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            pswd = form.cleaned_data['password1']
            print('{} {}'.format(username, pswd))
            user = authenticate(username=username, password=pswd)
            login(request, user)
            return redirect('usersIndex')
    else:
        form = UserCreationForm()
    context = {
       'form' : form
    }
    return render(request, 'users/register.html', context=context)