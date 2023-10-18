from rest_framework import status
from django.db import transaction
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

from .serializers import UserLoginSerializer, UserSignupSerializer, UserSerializer


class UserLoginView(APIView):

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        access_token = RefreshToken.for_user(user).access_token
        refresh_token = RefreshToken.for_user(user)
        user_data = UserSerializer(user).data
        return Response({
            "user_id": user_data['id'],
            "user_name": user_data['username'],
            "is_admin": user_data['is_superuser'],
            "access": str(access_token),
            "refresh": str(refresh_token)
        })


class UserSignupView(APIView):

    @transaction.atomic
    def post(self, request):
        serializer = UserSignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = User.objects.get(username=serializer.validated_data['username'])
        refresh = RefreshToken.for_user(user=user)
        user_data = UserSerializer(user).data
        return Response({
            "user_id": user_data['id'],
            "user_name": user_data['username'],
            "is_admin": user_data['is_superuser'],
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        })


class UserLogoutView(APIView):

    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh = request.data['refresh_token']
            token = RefreshToken(refresh)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserSearchView(APIView):

    def post(self, request):
        email = request.query_params.get('email')
        name = request.query_params.get('name')
        try:
            if email:
                user = User.objects.get(email=email)
            if name:
                user = User.objects.get(username__contains=name)
            user_data = UserSerializer(user).data
            return Response(user_data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response('User Does not Exists')
