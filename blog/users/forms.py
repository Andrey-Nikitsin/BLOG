
from django import forms
from django.contrib.auth import login, authenticate
from django.http import request
from users.models import Clients


class loginForm(forms.Form):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs = {'class' : 'input', 'placeholder' : 'имя пользователя'}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs = {'class' : 'input', 'placeholder' : 'пароль'}
        )
    )


    def clean(self):
        user  = authenticate(**dict(self.cleaned_data))
        if user is not None:
            self.user = user
            return self.cleaned_data
        else:
            self.add_error('username', 'неверное имя пользователя или пароль')
            raise forms.ValidationError('User not found')
    
    def auth(self, request):
        login(request, self.user)

class Register_user(forms.ModelForm):
    password_repeat = forms.CharField(
        widget=forms.PasswordInput(
            attrs = {'class' : 'input', 'placeholder' : 'пароль'}
        )
    )
    class Meta:
        model = Clients
        fields = {"username", "password", "email"}
        widgets = {
            "username" : forms.TextInput(
                attrs= {'class' : 'input', 'plaseholder' : 'имя пользователя'}
            )
        }

    def clean(self):
        if Register_user.is_valid:
            return self.cleaned_data
        else:
            self.add_error('username', 'fghdjkgfdgsafEGATRHD')
            raise forms.ValidationError('User not found')