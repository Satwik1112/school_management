from rest_framework import serializers
from .models import User


class Register_Serializer(serializers.Serializer):
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'subject']

        def validate(self, attrs):
            email = attrs.get('email', '')
            username = attrs.get('username', '')

            if not username.isalphanum():
                raise serializers.ValidationError('Username only contains alpha numeric characters')
            return attrs


        def create(self, validated_data):
            return User.Object.create_user(**validated_data)
