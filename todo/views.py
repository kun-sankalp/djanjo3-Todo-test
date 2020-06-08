from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate

def home(request):
     return render(request, 'todo/home.html')



def loginuser(request):

    if request.method == 'GET':
        return render(request, 'todo/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password = request.POST['password'])
        if user is None:
            return render(request, 'todo/loginuser.html', {'form': AuthenticationForm(), 'error':'Invalid Credentials'})
        else:
            login(request, user)
            return redirect('currenttodos')




def signupuser(request):
    if request.method == 'POST':
        #user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                #user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
                user.save()
                #return render(request, 'todo/signupuser.html', {'form': UserCreationForm(), 'success':'User created, Create a new USER?'})
                login(request, user)
                return redirect('currenttodos')


            except IntegrityError:
                return# render(request, 'todo/signupuser.html', {'form': UserCreationForm(), 'error':'username already in use'})

        else:
            #tell user password did not match
            return render(request, 'todo/signupuser.html', {'form': UserCreationForm(), 'error':'passwords did not match'})

    else:
        return render(request, 'todo/signupuser.html', {'form': UserCreationForm()})



def currenttodos(request):
     return render(request, 'todo/currenttodos.html')




def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
