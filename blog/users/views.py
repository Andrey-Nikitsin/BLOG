from distutils import dist
from unicodedata import name
from django.shortcuts import render
from django.template import context
from users.forms import loginForm, Register_user
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from users.models import Clients


def Multiform(request):
    if request.method == 'POST':
        Register_form = Register_user(request.POST)
        login_form = loginForm(request.POST)
        if Register_form.is_valid():
            Register_form.save()
            return redirect("user_login") 
        elif login_form.is_valid:
            user = authenticate(username =request.POST['username'], password=request.POST['password'])
            if user is not None:
                login(request, user)
                return redirect("hello")
    else:
        Register_form = Register_user()
        login_form = loginForm()

    return render(request, 'login.html', {'Register_form' : Register_form, 'login_form' : login_form})            


def index(request): 
    return render(request, 'login.html')

@login_required(login_url='/index/login')
def hello(request):
    contex = {
        "content" : request.user
    }
    return render(request, 'hello.html', contex) 