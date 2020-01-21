from django.db import models
from django.conf import settings

class Portfolio(models.Model):
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        default=1,
        on_delete=models.CASCADE
    )
    port_title = models.CharField(max_length=120)
    port_content = models.TextField(default="글을 쓰지 않았어요")
    port_date = models.DateTimeField(auto_now=True)
    # port_file = models.CharField(max_length=500)
    