from pyexpat import model
from rest_framework import serializers

from .models import *

class RegisteredMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = '__all__'