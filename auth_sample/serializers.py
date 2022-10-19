from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import AccessToken

from auth_sample.models import User


class UserSerializer(serializers.ModelSerializer):
    token = serializers.CharField(required=False)
    refresh = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'token',
            'refresh',
            'groups',
            'is_superuser'
        ]
        read_only_fields = [
            'token',
            'refresh',
            'user'
        ]
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        serializer = UserSerializer(data=validated_data)
        if serializer.is_valid():
            user = User.objects.create(
                username=validated_data['username'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
            )
            user.set_password(validated_data['password'])
            tokenr = TokenObtainPairSerializer().get_token(user)
            tokena = AccessToken().for_user(user)

            user.token = tokena
            user.refresh = tokenr

            user.save()
            return user
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
