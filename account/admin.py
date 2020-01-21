from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class accountAdmin(UserAdmin):
    model = User

admin.site.register(User, accountAdmin)


# class UserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'password','email','is_superuser')

# admin.site.register(User, UserAdmin)


# 출처: https://dlwodus.tistory.com/373 [MY MEMO]