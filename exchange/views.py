import email
from django.shortcuts import render
from .forms import Register_User, Login_Form
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


def Home(request):
    fm = Login_Form(request=request, data=request.POST)
    if fm.is_valid():
        username = fm.cleaned_data['username']
        userpassword = fm.cleaned_data['password']
        usr = authenticate(username=username, password=userpassword)
        if usr is not None:
            login(request, usr)
            return HttpResponseRedirect('/dashboard/')
    else:
        fm = Login_Form()
    return render(request, 'exchange/home.html', {'form': fm})


def Register_Form(request):
    if request.method == 'POST':
        form = Register_User(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dashboard/')
    else:
        form = Register_User()
    return render(request, 'exchange/registerform.html', {'form': form})


def Dashboard(request):
    return render(request, 'exchange/dashboard.html')


def Add_blogs(request):
    return render(request, 'exchange/addblogs.html')


def User_Profile(request):
    user = request.user

    return render(request, 'exchange/userprofile.html', {'user': user})


def Manage_Users(request):
    User = get_user_model()
    users = User.objects.all()
    return render(request, 'exchange/manageuser.html', {'users': users})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def Transaction_History(request):
    
    return render(request, 'exchange/transactionhistory.html')
