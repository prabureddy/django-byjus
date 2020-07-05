from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime
from grade.models import Grade
from django.core.exceptions import ValidationError


from django.contrib.auth.models import AbstractUser


def validate_mobile_number(value):
    if len(str(value)) >= 10 and len(str(value)) <= 13:
        return value
    else:
        raise ValidationError("Enter Correct Mobile Number.")


class User(AbstractUser):
    pass


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    grade = models.OneToOneField(Grade, on_delete=models.CASCADE)
    mobile = models.BigIntegerField(
        null=False, blank=False, validators=[validate_mobile_number])
    verify = models.BooleanField(default=False)

    def clean_mobile(self):

        mobile = self.mobile
        mobile = len(str(mobile))

        if mobile == 10:
            pass
        else:
            raise ValidationError("Enter Correct Mobile No.!!!")

        return mobile

        def __str__(self):
            return self.user.username


class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teach_for = models.ManyToManyField(Grade, blank=False)
    mobile = models.BigIntegerField(
        null=False, blank=False, validators=[validate_mobile_number])
    verify = models.BooleanField(default=False)

    def clean_mobile(self):

        mobile = self.mobile
        mobile = len(str(mobile))

        if mobile == 10:
            pass
        else:
            raise ValidationError("Enter Correct Mobile No.!!!")

        return mobile

        def __str__(self):
            return self.user.username
