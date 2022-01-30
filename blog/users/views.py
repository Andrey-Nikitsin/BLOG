from distutils import dist
from unicodedata import name
from django.shortcuts import render
from django.template import context
from users.forms import loginForm, Register_user
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from users.models import Clients
from django.contrib.auth import logout



def login_user(request):
    if request.method == 'POST':
        login_form = loginForm(request.POST)
        if login_form.is_valid():
            user = authenticate(username =request.POST['username'], password=request.POST['password'])
            if user is not None:
                login(request, user)
                return redirect("hello")        
    else:
        login_form = loginForm()

    return render(request, 'login.html', {'login_form' : login_form})


def register(request):
    if request.method == 'POST':
        Register_form = Register_user(request.POST)
        if Register_form.is_valid():
            Register_form.save()
            return redirect("user_login")
    else:
        Register_form = Register_user()
    return render(request, 'register.html', {'Register_form' : Register_form})            


def index(request): 
    return render(request, 'login.html')

@login_required(login_url='/index')
def hello(request):
    contex = {
        "content" : request.user
    }
    return render(request, 'hello.html', contex) 