from django.contrib import admin

# Register your models here.
from django.contrib import admin
from practice.models import *

class User_admin(admin.ModelAdmin):
    list_display = ('id', 'User_Name', 'User_Email', 'User_Password', 'User_Authorized', 'created', 'last_come_date')

class Authorized_admin(admin.ModelAdmin):
    list_display = ('id', 'Authorized', )


admin.site.register(User, User_admin)
admin.site.register(Authorized, Authorized_admin)