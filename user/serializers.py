from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
# from django.conf import settings
# settings.AUTH_USER_MODEL

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True, required=True)
    first_name = serializers.CharField(required=True)

    
    
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
    
def validate(self, data):
    if data ['password'] != data['password2']:
        raise serializers.ValidationError(
            {'passwork':'Password fields didnt match.'}
        )
    return data    

def create(self, validated_data):
    validated_data.pop('password2')  # password2 kullanılmayacağı için dictten çıkardık
    password =  validated_data.pop('password2')  # passwordu daha sonra set etmek için değişkene atadık.
    user = User.objects.create(**validated_data) # username=validated_data['username], email. = va...
    user.set_password(password)  # passwordun encrypte olarak db ye kaydedilmesini sağlıyor
    user.save()
    return user