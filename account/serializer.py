from .models import User
from rest_framework import serializers


class accountSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        #fields = "__all__"
        fields = ('user_id','password','email','user_type')

