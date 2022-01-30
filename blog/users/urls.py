from django.urls import path
from users.views import login_user, hello, register

urlpatterns = [
    path('', login_user, name = 'user_login'),
    path('hello/', hello, name = 'hello' ),
    path('register/', register, name = 'registration')
]
