from django.shortcuts import render
from django.template import context
from users.forms import loginForm

def login(request):
    context = {'login_form' : loginForm()}
    # if request.method == "POST":
    #     login_form = loginForm(request.POST)

    return render(request, 'login.html', context)

def index(request):
    return render(request, 'base.html')

def andrey(request):
    return render(request, 'andrey.html')  