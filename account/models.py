from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser # 커스텀 유저를 위한 라이브러리

# class account(models.Model):
#     user_id = models.CharField(max_length=100, null='false')
#     user_name = models.CharField(max_length=50)
#     user_pswd = models.TextField()
#     user_email = models.TextField()
#     user_type = models.IntegerField()

class User(AbstractUser): #기존 user모델에서 확장되는 형태라 하나만 추가해주면 되어요.
    user_type = models.IntegerField(null=True)
