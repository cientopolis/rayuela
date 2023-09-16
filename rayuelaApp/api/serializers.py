from rest_framework import serializers
from rayuelaApp.models.user import User
from rayuelaApp.models.project import Project


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    admins = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='username'
     )

    class Meta:
        model = Project
        fields = '__all__'

