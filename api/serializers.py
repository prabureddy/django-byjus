from rest_framework import serializers
from accounts.models import User

from accounts.models import StudentProfile, TeacherProfile

from django.core.exceptions import ValidationError


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
