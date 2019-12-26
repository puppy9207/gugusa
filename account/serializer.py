from .models import account
from rest_framework import serializers


class accountSerializer(serializers.ModelSerializer):

    class Meta:
        model = account
        fields = "__all__"
