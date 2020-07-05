from rest_framework import routers
from django.urls import path, include

from api.serializers_views import registration, studentRegistration, teacherRegistration

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

app_name = "api"

urlpatterns = [
    path('docs/', schema_view),
    path('signup/usersignup/', registration, name='user-signup'),
    path('signup/usersignup/student/', studentRegistration, name='user-signup'),
    path('signup/usersignup/teacher/', teacherRegistration, name='user-signup'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
