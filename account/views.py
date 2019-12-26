from rest_framework import viewsets
from .models import User
from .serializer import accountSerializer


class accountViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = accountSerializer