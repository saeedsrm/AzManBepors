from rest_framework import serializers, status
from .models import CustomUser, Responder
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from adviser.custom_relational_fields import UserEmailNameRelationalField


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=False,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = "__all__"


    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        try:
            validated_data['city'] == ''
        except:
            validated_data['city'] = None

        try:
            validated_data['province'] == ''
        except:
            validated_data['province'] = None
        try:
            validated_data['collage'] == ''
        except:
            validated_data['collage'] = None
        try:
            validated_data['entering_year'] == ''
        except:
            validated_data['entering_year'] = None
        try:
            validated_data['username'] == ''
        except:
            validated_data['username'] = None
        try:
            validated_data['student_code'] == ''
        except:
            validated_data['student_code'] = None
        try:
            validated_data['first_name'] == ''
        except:
            validated_data['first_name'] = None
        try:
            validated_data['last_name'] == ''
        except:
            validated_data['last_name'] = None
        try:
            validated_data['major'] == ''
        except:
            validated_data['major'] = None
        try:
            validated_data['fullname'] == ''
        except:
            validated_data['fullname'] = None
        try:
            validated_data['email'] == ''
        except:
            validated_data['email'] = None

        user = CustomUser.objects.create(
            username=validated_data['username'],
            student_code=validated_data['student_code'],
            phone_number=validated_data['phone_number'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            major=validated_data['major'],
            city=validated_data['city'],
            province=validated_data['province'],
            is_active=validated_data['is_active'],
            collage=validated_data['collage'],
            entering_year=validated_data['entering_year'],
            fullname=validated_data['fullname']
        )

        user.set_password(validated_data['password'])
        user.save()
        print(validated_data)

        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['phone_number'] = user.phone_number
        return token


class ResponderSerializer(serializers.ModelSerializer):
    user = UserEmailNameRelationalField(read_only=True)

    class Meta:
        model = Responder
        fields = '__all__'

    # def save(self):
    #     user = self.context['request.user']
    #     fields_of_activity = self.validated_data['fields_of_activity']
    #     interests = self.validated_data['interests']
    #     descriptions = self.validated_data['descriptions']
    #     responder = Responder.objects.create(user=user, fields_of_activity=fields_of_activity, interests=interests,
    #                                          descriptions=descriptions)
    #     responder.save()
    #     return responder
