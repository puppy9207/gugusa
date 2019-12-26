from .models import Project
from rest_framework import serializers
from rest_framework.parsers import MultiPartParser, FormParser

class ProjectSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='user_id.username')

    class Meta:
        model = Project
        fields = ('pk','pro_title','pro_content','pro_date','pro_link','pro_sub','author')