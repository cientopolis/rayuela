from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from users.models import Volunteer
from rayuelaApp.models.project import Project
from rayuelaApp.models.task_type import TaskType
from rayuelaApp.models.project_subarea import ProjectSubArea
from rayuelaApp.models.check_in import CheckIn
from rayuelaApp.models.collection_task import CollectionTask

class TaskTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskType
        fields = '__all__'


class ProjectSubAreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectSubArea
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    admins = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='username'
     )

    task_types = TaskTypeSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = '__all__'


class VolunteerSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(read_only=True, many=True)

    class Meta:
        model = Volunteer
        fields = ['id', 'projects', 'username', 'email', 'password', 'profile_image', 'first_name', 'last_name']

    def create(self, validated_data):
        user = Volunteer.objects.create(email=validated_data['email'], username=validated_data['username'], password=make_password(validated_data['password']))
        return user


class CheckinSerializer(serializers.ModelSerializer):

    class Meta:
        model = CheckIn
        fields = '__all__'

class CollectionTaskSerializer(serializers.ModelSerializer):
    task_type = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
     )

    sub_area = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='number'
     )

    time_restriction = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
     )

    class Meta:
        model = CollectionTask
        fields = '__all__'
