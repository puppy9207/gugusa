from .models import User
from rest_framework import serializers
from django.contrib.auth import get_user_model

class accountSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        #fields = "__all__"
        fields = ('username','password','email','user_type',)

