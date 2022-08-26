from copy import copy

from rest_framework import serializers, validators
from .models import CreateNewQuestion, Category, Tag, Answer
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .custom_relational_fields import *


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    author = AuthorEmailNameRelationalField(read_only=True)
    question = QuestionAnswerRelationalField(read_only=True)

    class Meta:
        model = Answer
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()
    category = serializers.SlugRelatedField(slug_field='name', queryset=Category.objects.all())
    tag = serializers.SlugRelatedField(slug_field='name', queryset=Tag.objects.all())
    author = UserEmailNameRelationalField(read_only=True)

    class Meta:
        model = CreateNewQuestion
        fields = '__all__'

    def get_answers(self, obj):
        result = obj.answers.all()
        return AnswerSerializer(instance=result, many=True).data
    #
    # def run_validators(self, value):
    #     for validator in self.validators:
    #         if isinstance(validator, validators.UniqueTogetherValidator):
    #             self.validators.remove(validator)
    #     super(QuestionSerializer, self).run_validators(value)

    # def create(self, validated_data):
    #     category = Category.objects.get_or_create(validated_data['category'])
    #     print(category)
    #     tag = Tag.objects.get_or_create(validated_data['tag'])
    #     question = CreateNewQuestion.objects.create(
    #
    #         category=category, tag=tag, question=validated_data['question'], status=validated_data['status']
    #     )
    #     question.save(author=validated_data['request'].user)
    #     print(question)
    #
    #     return question
