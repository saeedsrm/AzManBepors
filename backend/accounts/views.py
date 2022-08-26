from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from permission import IsOwner
from .models import CustomUser, Responder
from .serializers import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import RegisterSerializer, ResponderSerializer
from rest_framework import generics, status
from django.db.models import Q


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
        srz_data = UserSerializer(instance=user, data=request.data, partial=True)
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


class CreateResponder(generics.CreateAPIView):
    queryset = Responder.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ResponderSerializer

    def post(self, request):
        srz_data = ResponderSerializer(data=request.data)
        if srz_data.is_valid():
            user = CustomUser.objects.filter(pk=request.user.id)
            if user:
                print(user)
                filtering = user.filter(Q(first_name='') |
                                        Q(last_name='') |
                                        Q(fullname='') |
                                        Q(username='') | Q(email='') |
                                        Q(collage='') |
                                        Q(major='') | Q(province='') | Q(phone_number='') |
                                        Q(city='') | Q(entering_year=None))

                if filtering:
                    return Response("please complete your profile")
                else:

                    srz_data.save(user=request.user)
                    print(filtering)

                    return Response(srz_data.data, status=status.HTTP_201_CREATED)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)
