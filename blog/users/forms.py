
from django import forms
from django.contrib.auth import login, authenticate
from django.http import request
from users.models import Clients
from django.core.exceptions import ValidationError

class loginForm(forms.Form):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs = {'class' : 'input', 'placeholder' : 'имя пользователя'}
        ),
        empty_value = '1'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs = {'class' : 'input', 'placeholder' : 'пароль'}
        ),
        empty_value = '1'
    )


    def clean(self):
        super().clean()
        errors = {}
        if len(self.cleaned_data['username'])<4:
            errors['username'] = ValidationError('Слишком короткое имя пользователя')
        if len(self.cleaned_data['password']) < 4:
            errors['password'] = ValidationError('Слишком короткий пароль')
        if errors:
            raise ValidationError(errors)
    

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
        super().clean()
        errors = {}
        if len(self.cleaned_data['username'])<4:
            errors['username'] = ValidationError('Слишком короткое имя пользователя')
        if len(self.cleaned_data['password']) < 4:
            errors['password'] = ValidationError('Слишком короткий пароль')
        if errors:
            raise ValidationError(errors)