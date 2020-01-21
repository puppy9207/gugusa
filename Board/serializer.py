from .models import Board
from rest_framework import serializers
from rest_framework.parsers import MultiPartParser, FormParser

class BoardSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='user_id.username')

    class Meta:
        model = Board
        fields = ('pk','brd_title','brd_content','brd_date','author')
