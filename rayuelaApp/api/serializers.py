from rest_framework import serializers
from users.models import Volunteer
from rayuelaApp.models.project import Project
from rayuelaApp.models.check_in import CheckIn


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
        fields = ['id', 'projects', 'username', 'email', 'profile_image', 'complete_name']

    def create(self, validated_data):
        user = Volunteer.objects.create(email=validated_data['email'], username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class CheckinSerializer(serializers.ModelSerializer):

    class Meta:
        model = CheckIn
        fields = '__all__'
