from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from permission import IsOwner
from .models import CustomUser
from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import RegisterSerializer, ResponderSerializer
from rest_framework import generics, status


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class UserUpdateView(APIView):
    permission_classes = [IsOwner, ]

    def put(self, request):
        user = CustomUser.objects.get(email=request.user)
        self.check_object_permissions(request, user)
        srz_data = RegisterSerializer(instance=user, data=request.data, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_200_OK)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDeleteView(APIView):
    permission_classes = [IsOwner, ]

    def delete(self, request):
        user = CustomUser.objects.get(email=request.user)
        self.check_object_permissions(request, user)
        user.delete()
        return Response({'message': 'user deleted'}, status=status.HTTP_200_OK)


class CreateResponder(APIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = ResponderSerializer

    def post(self, request):
        srz_data = ResponderSerializer(data=request.data)
        if srz_data.is_valid():
            user = self.context['request'].user
            # filtering = CustomUser.objects.filter(first_name__isnull=False, last_name__isnull=False,
            #                                       fullname__isnull=False,
            #                                       username__isnull=False, email__isnull=False, collage__isnull=False,
            #                                       major__isnull=False, province__isnull=False, city__isnull=False,
            #                                       entering_year__isnull=False, phone_number__isnull=False,
            #                                       student_code__isnull=False)
            # if filtering:
            #     return Response("please complete your profile")
            # else:

            srz_data.save(user=user)
            print(user)
            return Response(srz_data.data, status=status.HTTP_201_CREATED)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)
