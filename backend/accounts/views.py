from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from permission  import  IsOwner
from .models import CustomUser
from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import RegisterSerializer
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

    def put(self, request, pk):
        user = CustomUser.objects.get(pk=pk)
        self.check_object_permissions(request, user)
        srz_data = RegisterSerializer(instance=user, data=request.data, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_200_OK)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDeleteView(APIView):
    permission_classes = [IsOwner, ]

    def delete(self, request, pk):
        user = CustomUser.objects.get(pk=pk)
        self.check_object_permissions(request, user)
        user.delete()
        return Response({'message': 'user deleted'}, status=status.HTTP_200_OK)
