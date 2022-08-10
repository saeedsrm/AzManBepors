from django.shortcuts import render
from .serializers import *
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from permission import IsOwnerOrReadOnly


class CategoryCreateView(APIView):
    """
        Create a new question
    """
    permission_classes = [IsAuthenticated, ]
    serializer_class = CategorySerializer

    def post(self, request):
        srz_data = CategorySerializer(data=request.data)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_201_CREATED)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class TagCreateView(APIView):
    """
        Create a new question
    """
    permission_classes = [IsAuthenticated, ]
    serializer_class = TagSerializer

    def post(self, request):
        srz_data = TagSerializer(data=request.data)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_201_CREATED)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionListView(APIView):

    def get(self, request):
        questions = CreateNewQuestion.objects.all()
        srz_data = QuestionSerializer(instance=questions, many=True).data
        return Response(srz_data, status=status.HTTP_200_OK)


class QuestionCreateView(APIView):
    """
        Create a new question
    """
    permission_classes = [IsAuthenticated, ]
    serializer_class = QuestionSerializer

    def post(self, request):
        srz_data = QuestionSerializer(data=request.data)
        if srz_data.is_valid():
            srz_data.save(author=request.user)
            return Response(srz_data.data, status=status.HTTP_201_CREATED)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionUpdateView(APIView):
    permission_classes = [IsOwnerOrReadOnly, ]

    def put(self, request, pk):
        question = CreateNewQuestion.objects.get(pk=pk)
        self.check_object_permissions(request, question)
        srz_data = QuestionSerializer(instance=question, data=request.data, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_200_OK)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDeleteView(APIView):
    permission_classes = [IsOwnerOrReadOnly, ]

    def delete(self, request, pk):
        question = CreateNewQuestion.objects.get(pk=pk)
        self.check_object_permissions(request, question)
        question.delete()
        return Response({'message': 'question deleted'}, status=status.HTTP_200_OK)
