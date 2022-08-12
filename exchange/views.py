import email
from django.shortcuts import render
from .forms import Register_User, Login_Form
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from api.models import Order

# User login form into home page


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


# User register form

def Register_Form(request):
    if request.method == 'POST':
        form = Register_User(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dashboard/')
    else:
        form = Register_User()
    return render(request, 'exchange/registerform.html', {'form': form})


# User dashboard

def Dashboard(request):
    return render(request, 'exchange/dashboard.html')


# Write blogs as admin panel

def Add_blogs(request):
    return render(request, 'exchange/addblogs.html')

# Every user profile


def User_Profile(request):
    user = request.user

    return render(request, 'exchange/userprofile.html', {'user': user})


# Manage all user data

def Manage_Users(request):
    User = get_user_model()
    users = User.objects.all()
    return render(request, 'exchange/manageuser.html', {'users': users})


# User logout

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


# User transactin history

def Transaction_History(request):
    email = request.user.email
    orders = Order.objects.filter(email=email)
    print(orders)
    return render(request, 'exchange/transactionhistory.html',{'orders':orders})


# User pending order or paid order

def Manage_Order(request):

    bkash = Order.objects.filter(receive_method='Bkash')
    nagad = Order.objects.filter(receive_method='Nagad')
    rocket = Order.objects.filter(receive_method='Rocket')
    upay = Order.objects.filter(receive_method='Upay')
    vm = Order.objects.filter(receive_method='Visa/Master card')
    print(nagad)
    print(bkash)
    return render(request, 'exchange/manageorder.html', {'bkash': bkash, 'nagad': nagad,
                                                         'rocket': rocket, 'upay': upay, 'vm': vm, })


# Change user password

def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                return HttpResponseRedirect('/user-profile/')
        else:
            fm = PasswordChangeForm(user=request.user)
            return render(request, 'exchange/changepassword.html', {'form': fm})
    else:
        HttpResponseRedirect('/dashboard')
