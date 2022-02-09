from django.urls import path
from users.views import Multiform, hello

urlpatterns = [
    path('', Multiform, name = 'user_login'),
    path('hello/', hello, name = 'hello' ),
]
