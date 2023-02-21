from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import Post, Comments, Up
from django import core
# Serializer to Get User Details using Django Token Authentication


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username"]


# Serializer to Register User
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2',
                  'email')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class CommentSerialization(serializers.ModelSerializer):
    name = serializers.CharField(source='username')

    class Meta:
        model = Comments
        fields = "__all__"


class UpsSerialization(serializers.ModelSerializer):
    name = serializers.CharField(source='username')
    comments = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Up
        fields = "__all__"


class PostSerialization(serializers.ModelSerializer):
    name = serializers.CharField(source='username')
    comments = CommentSerialization(many=True, read_only=True)
    ups = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = "__all__"
