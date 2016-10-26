from django.contrib import admin
from .models import Profil
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class UserProfilInline(admin.StackedInline):
    model = Profil


class UserProfilAdmin(UserAdmin):
    list_display = ['first_name', 'last_name', 'email']
    list_filter = ['last_name']
    inlines = [UserProfilInline]

admin.site.unregister(User)
admin.site.register(User, UserProfilAdmin)

