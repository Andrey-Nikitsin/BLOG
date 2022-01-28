from distutils import dist
from django.shortcuts import render
from django.template import context
from users.forms import loginForm, Register_user
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate


# def register(request):
#     context = {'register_form' : Register_user() }
#     if request.method == "POST":
#         register_form = Register_user(request.POST)
#         print(register_form)
#         if register_form.is_valid():
#             return redirect("andrey")
#         context.update(register_form = register_form)
#     return render(request, 'register.html', context)

def Multiform(request):
    if request.method == 'POST':
        Register_form = Register_user(request.POST)
        login_form = loginForm(request.POST)
        if Register_form.is_valid():
            Register_form.save()
            return redirect("hello") 
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
    return render(request, 'hello.html') 