from django.contrib import admin
from users.models import Clients
from django.contrib.auth.admin import UserAdmin

admin.site.register(Clients, UserAdmin)
