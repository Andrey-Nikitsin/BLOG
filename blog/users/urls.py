from django.urls import path
from users.views import Multiform, hello, index

urlpatterns = [
    path('', index),
    path('login/', Multiform, name= 'user_login'),
    path('hello/', hello, name = 'hello' ),
    # path('register/', register, name = 'registration')
]
