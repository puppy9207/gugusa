from rest_framework import viewsets
from .models import account
from .serializer import accountSerializer


class accountViewSet(viewsets.ModelViewSet):
    queryset = account.objects.all()
    serializer_class = accountSerializer