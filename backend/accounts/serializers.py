from rest_framework import serializers
from .models import CustomUser
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = "__all__"
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'phone_number': {'required': True},
            'student_code': {'required': True},
            'email': {'required': True},
            'username': {'required': True},
            'major': {'required': True},
            'is_active': {'required': True},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['username'],
            student_code=validated_data['student_code'],
            phone_number=validated_data['phone_number'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            major=validated_data['major'],
            is_active=validated_data['is_active'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return Response({
            "user": user,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token
