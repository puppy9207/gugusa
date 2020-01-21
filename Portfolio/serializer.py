from .models import Portfolio
from rest_framework import serializers
from rest_framework.parsers import MultiPartParser, FormParser

class PortfolioSerializer(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(source='user_id.username')

    class Meta:
        model = Portfolio
        fields = ('pk','port_title','port_content','port_date','author')
