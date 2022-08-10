from django.shortcuts import render
from .forms import Register_User
from django.http import HttpResponse, HttpResponseRedirect


def Home(request):
    return render(request, 'exchange/home.html')


def Register_Form(request):
    if request.method == 'POST':
        form = Register_User(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dashboard/')
    else:
        form = Register_User()
    return render(request, 'exchange/registerform.html', {'form': form})
