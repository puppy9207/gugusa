from django.db import models
from django.conf import settings

class Project(models.Model):
    pro_title = models.CharField(max_length=120)
    pro_content = models.TextField(default="글을 쓰지 않았어요")
    pro_date = models.DateTimeField(auto_now=True)
    pro_link = models.CharField(max_length=250,null=True)
    pro_sub = models.IntegerField(default=0,null=True)
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        default=1,
        on_delete=models.CASCADE
    )

# Create your models here.
