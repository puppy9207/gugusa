from django.contrib import admin
from .models import User
# Register your models here.

admin.site.register(User)


# class UserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'password','email','is_superuser')

# admin.site.register(User, UserAdmin)


# 출처: https://dlwodus.tistory.com/373 [MY MEMO]