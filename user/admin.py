from django.contrib import admin
from django.contrib import admin
from .models import User
# Register your models here.

#
# class UserAdmin
#
# class UserAdmin(admin.ModelAdmin):
#     list_display = {'name' , 'email' ,'phone_no' , 'profile_picture'}
admin.site.register(User)