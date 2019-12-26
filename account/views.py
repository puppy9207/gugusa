from rest_framework import viewsets, generics
from .models import User
from .serializer import accountSerializer
from django.contrib.auth import get_user_model


User = get_user_model()

class accountViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = accountSerializer