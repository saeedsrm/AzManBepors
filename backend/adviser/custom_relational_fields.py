from rest_framework import serializers


class UserEmailNameRelationalField(serializers.RelatedField):
    def to_representation(self, value):
        return f'{value.username} - {value.email}'


class QuestionTagNameRelationalField(serializers.RelatedField):
    def to_representation(self, value):
        return f'{value.name}'


class QuestionCategoryNameRelationalField(serializers.RelatedField):
    def to_representation(self, value):
        return f'{value.name}'
