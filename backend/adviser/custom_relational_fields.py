from rest_framework import serializers


class UserEmailNameRelationalField(serializers.RelatedField):
    def to_representation(self, value):
        return f'{value.phone_number}'


class AuthorEmailNameRelationalField(serializers.RelatedField):
    def to_representation(self, value):
        return f'{value.user.phone_number}'


class QuestionTagNameRelationalField(serializers.RelatedField):
    def to_representation(self, value):
        return f'{value.name}'


class QuestionCategoryNameRelationalField(serializers.RelatedField):
    def to_representation(self, value):
        return f'{value.name}'


class QuestionAnswerRelationalField(serializers.RelatedField):
    def to_representation(self, value):
        return f'{value.id}'
