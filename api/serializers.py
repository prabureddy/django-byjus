from rest_framework import serializers
from accounts.models import User

from accounts.models import StudentProfile, TeacherProfile

from django.core.exceptions import ValidationError

class CheckEmailExists(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email',
        ]


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'password',
            'first_name',
            'last_name',
            'email',
        ]
        extra_kwargs = {'password': {'write_only': True}, 'email': {
            'required': True}, 'first_name': {'required': True}, 'last_name': {'required': True}, }

    def validate_email(self, value):
        if self.context['request']._request.method == 'POST':
            if self.Meta.model.objects.filter(username=value).exists():
                raise ValidationError('A Email with this name already exists.')
        return value
    
    def validate_first_name(self, value):
        if self.context['request']._request.method == 'POST':
            if len(value) < 4:
                raise ValidationError('First Name should be greater than 4.')
        return value

    def validate_last_name(self, value):
        if self.context['request']._request.method == 'POST':
            if len(value) < 4:
                raise ValidationError('Last Name should be greater than 4.')
        return value
    
    def validate_password(self, value):
        if self.context['request']._request.method == 'POST':
            if len(value) < 8 and len(value) < 20:
                raise ValidationError('Password should be greater than 8 and less than 20')
        return value

    def create(self, validated_data):

        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        instance.username = validated_data['email']
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance


class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = '__all__'

class TeacherProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherProfile
        fields = '__all__'


from grade.models import Grade
class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'


from grade.models import Program
class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'
