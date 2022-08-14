import email
from django.shortcuts import render

import exchange
from .forms import Register_User, Login_Form
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm
from api.models import Order, Blog, Review
from .forms import Order_Form, Blog_Form, Review_Form
from django.conf import settings
from sslcommerz_lib import SSLCOMMERZ
from django.urls import reverse

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
            print(form)
            return HttpResponseRedirect('home')
    else:
        form = Register_User()
    return render(request, 'exchange/registerform.html', {'form': form})


# User dashboard

def Dashboard(request):
    form = Order_Form()
    if request.method == 'POST':
        form = Order_Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/transaction_history/')
    else:
        form = Order_Form()
    return render(request, 'exchange/dashboard.html', {'form': form})


# Write blogs as admin panel

def Add_blogs(request):
    blogs = Blog.objects.all()
    email = request.user.email
    reviews = Review.objects.filter(email=email)
    rform = Review_Form()
    bform = Blog_Form()
    if request.method == 'POST':
        bform = Blog_Form(request.data)
        if bform.is_valid():
            bform.save()
    if request.method == 'POST':
        rform = Review_Form(request.data)
        if rform.is_valid():
            print(rform)
            rform.save()
    return render(request, 'exchange/addblogs.html', {'blogs': blogs, 'bform': bform, 'reviews': reviews, 'rform': rform})

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
    bkash = Order.objects.filter(receive_method='Bkash', status='paid')

    print(orders)
    return render(request, 'exchange/transactionhistory.html', {'orders': orders, 'bkash': bkash})


# User pending order or paid order
def update_order(request, pk):
    bk = Order.objects.get(id=pk)
    bk.status = 'paid'
    bk.save()
    return render(request, 'exchange/singledata.html', {'update': bk})


def Manage_Order(request):

    bkash = Order.objects.filter(receive_method='Bkash', status='pending')
    nagad = Order.objects.filter(receive_method='Nagad')
    rocket = Order.objects.filter(receive_method='Rocket')
    upay = Order.objects.filter(receive_method='Upay')
    vm = Order.objects.filter(receive_method='Visa/Master card')
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


def Exchange_Money(request):
    def amount():
        orders = Order.objects.filter(email=email)
        for am in orders:
            return am.receive_amount

    def number():
        orders = Order.objects.filter(email=email)
        for am in orders:
            return am.contact_number
    email = request.user.email
    orders = Order.objects.filter(email=email)
    name = request.user.first_name, request.user.last_name,
    print(amount(), number())
    # ssl coomerze
    settings = {'store_id': 'testbox',
                'store_pass': 'qwerty', 'issandbox': True}
    sslcommez = SSLCOMMERZ(settings)
    post_body = {}
    post_body['total_amount'] = amount()
    post_body['currency'] = "BDT"
    post_body['tran_id'] = "12345"
    post_body['success_url'] = "transaction_history"
    post_body['fail_url'] = "your fail url"
    post_body['cancel_url'] = "your cancel url"
    post_body['emi_option'] = 0
    post_body['cus_name'] = name
    post_body['cus_email'] = email
    post_body['cus_phone'] = number()
    post_body['cus_add1'] = orders
    post_body['cus_city'] = "Dhaka"
    post_body['cus_country'] = "Bangladesh"
    post_body['shipping_method'] = "NO"
    post_body['multi_card_name'] = ""
    post_body['num_of_item'] = 1
    post_body['product_name'] = "Test"
    post_body['product_category'] = "Test Category"
    post_body['product_profile'] = "general"

    response = sslcommez.createSession(post_body)
    # print(response)
    if request.method == 'POST':
        form = Order_Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect((response['GatewayPageURL']))
    else:
        form = Order_Form()
    return render(request, 'exchange/exchangemoney.html', {'form': form})
