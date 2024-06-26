from rest_framework import serializers
from users.models import Volunteer
from rayuelaApp.models.project import Project


class ProjectSerializer(serializers.ModelSerializer):
    admins = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='username'
     )

    class Meta:
        model = Project
        fields = '__all__'


class VolunteerSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(read_only=True, many=True)

    class Meta:
        model = Volunteer
        fields = '__all__'

    def create(self, validated_data):
        user = Volunteer.objects.create(email=validated_data['email'], username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    def add_project(self, user, project):
        user.add_project(project)
        self.save()


