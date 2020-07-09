from grade.models import Program
from grade.models import Grade
from django.contrib.auth import get_user_model
from rest_framework import viewsets, response, decorators, permissions, status, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import *
from accounts.models import User


@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def registration(request):
    serializer = UserCreateSerializer(
        data=request.data, context={'request': request})
    if not serializer.is_valid():
        return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    user = serializer.save()
    
    res = {
        'user': user.id,
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


class GradeViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = [permissions.AllowAny]


class ProgramViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = [permissions.AllowAny]


class CheckEmailExistsViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = CheckEmailExists
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        email = self.request.query_params.get('email')
        queryset = User.objects.filter(email=email)
        return queryset
