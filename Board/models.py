from django.db import models
from django.conf import settings

class Board(models.Model):
    brd_title = models.CharField(max_length=120)
    brd_content = models.TextField(default="글을 쓰지 않았어요")
    brd_date = models.DateTimeField(auto_now=True)
    # brd_count = models.IntegerField(default=0,null=True)
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        default=1,
        on_delete=models.CASCADE
    )