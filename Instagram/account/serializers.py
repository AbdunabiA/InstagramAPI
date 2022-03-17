from django.core.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
from .models import *

class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
    def validate_name(self, value):
        if len(value) == 0:
            raise ValidationError("Please write your name")
        return value