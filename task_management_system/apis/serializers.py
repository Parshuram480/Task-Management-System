from rest_framework import serializers
from django.contrib.auth.models import User
from usertask.models import AddTask


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddTask
        fields = "__all__"


class AddTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddTask
        fields = ['title', 'description', 'status']
