from pyexpat import model
from rest_framework import serializers

from .models import *

class RegisteredMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = '__all__'
        
        
class RevenuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revenues
        fields = '__all__'
        
        
class ExpendituresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenditures
        fields = '__all__'