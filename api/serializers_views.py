from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework import response, decorators, permissions, status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserCreateSerializer, StudentProfileSerializer, TeacherProfileSerializer
from accounts.models import User

@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def registration(request):
    serializer = UserCreateSerializer(data=request.data, context={'request': request})
    if not serializer.is_valid():
        return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)        
    # user = serializer.save()
    # refresh = RefreshToken.for_user(user)
    res = {
        # "refresh": str(refresh),
        # "access": str(refresh.access_token),
        "status": "SUCCESS"
    }
    return response.Response(res, status.HTTP_201_CREATED)


@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def studentRegistration(request):
    serializer = StudentProfileSerializer(
        data=request.data, context={'request': request})
    if not serializer.is_valid():
        return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    serializer.save()
    user = User.objects.get(pk=request.data['user'])
    refresh = RefreshToken.for_user(user)
    res = {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
        "status": "SUCCESS"
    }
    return response.Response(res, status.HTTP_201_CREATED)


@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def teacherRegistration(request):
    serializer = TeacherProfileSerializer(
        data=request.data, context={'request': request})
    if not serializer.is_valid():
        return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    serializer.save()
    user = User.objects.get(pk=request.data['user'])
    refresh = RefreshToken.for_user(user)
    res = {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
        "status": "SUCCESS"
    }
    return response.Response(res, status.HTTP_201_CREATED)
