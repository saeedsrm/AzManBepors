from rest_framework import serializers
from .models import CustomUser, Responder
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from adviser.custom_relational_fields import UserEmailNameRelationalField

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
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        try:
            validated_data['city'] == ''
        except:
            validated_data['city'] = "null"

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
            entering_year=validated_data['entering_year']
        )

        user.set_password(validated_data['password'])
        user.save()
        print(validated_data)

        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
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
