from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
# from django.conf import settings
# settings.AUTH_USER_MODEL

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True, required=True)
    
    
class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
            'password2'
        )
