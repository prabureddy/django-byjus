from django.contrib import admin
from .models import StudentProfile, TeacherProfile

from django.contrib.auth.admin import UserAdmin
from .models import  User


admin.site.register(User, UserAdmin)
admin.site.register(StudentProfile)
admin.site.register(TeacherProfile)
