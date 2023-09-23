from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone', 'email', 'username', 'password']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone', 'email', 'username', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = self.model(**validated_data)
        if password is not None:
            user.set_password(password)
        user.save()
        return user


