from django.db import models
from django.conf import settings

class account(models.Model):
    user_id = models.CharField(max_length=100, null='false')
    user_name = models.CharField(max_length=50)
    user_pswd = models.TextField()
    user_email = models.TextField()
    user_type = models.IntegerField()