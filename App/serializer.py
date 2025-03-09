# serializers.py
from rest_framework.serializers import *
from .models import *

class DefaultSerializer(ModelSerializer):
    class Meta:
        model = 'default'
        fields = '__all__'

class AccountSerializer(ModelSerializer):
    class Meta:
        model = 'account'
        fields = '__all__'

class PropertySerializer(ModelSerializer):
    class Meta:
        model = 'property'
        fields = '__all__'