from django.urls import path
from users.views import login, andrey, index

urlpatterns = [
    path('', index),
    path('login/', login ),
    path('andrey/', andrey )
]
