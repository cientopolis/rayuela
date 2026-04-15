from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from rayuelaApp.models.game_profile import GameProfile
from rayuelaApp.models.leaderboard import Competition
from rayuelaApp.models.score_allocation_strategy import ScoreAllocationStrategy
from users.models import Volunteer
from rayuelaApp.models.project import Project
from rayuelaApp.models.task_type import TaskType
from rayuelaApp.models.project_subarea import ProjectSubArea
from rayuelaApp.models.check_in import CheckIn
from rayuelaApp.models.collection_task import CollectionTask
from rayuelaApp.models.game_move import GameMove

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
    user = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='username'
     )

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

class GameMoveSerializer(serializers.ModelSerializer):

    class Meta:
        model = GameMove
        fields = '__all__'

    @staticmethod
    def is_contribution(checkin, task_type):
        contribution = False
        collection_tasks = CollectionTask.objects.filter(task_type=task_type['id'])
        for collection_task in collection_tasks:
            if (collection_task.sub_area.is_valid_area(checkin.latitude, checkin.longitude)
                    and collection_task.time_restriction.is_valid_time(checkin.datetime) and not collection_task.completed):
               contribution = True
        return contribution

    def create(self, validated_data):
        user = Volunteer.objects.get(id=validated_data['user'])
        project = Project.objects.filter(id=validated_data['project'])
        task_type = TaskType.objects.filter(id=validated_data['task_type'])
        checkin = CheckIn.objects.create(user=user, latitude=validated_data['latitude'], longitude=validated_data['longitude'],
                                         datetime=str(validated_data['datetime']), project=project.first(), task_type=task_type.first())
        collection_task = None
        points = 0
        badge = None

        if GameProfile.objects.filter(user=user):
            game_profile = GameProfile.objects.get(user=user)
        else:
            game_profile = GameProfile.objects.create(user=user)

        if self.is_contribution(checkin, task_type.values()[0]):
            collection_tasks = CollectionTask.objects.filter(task_type=task_type.values()[0]['id'])
            for collection_task_for in collection_tasks:
                if collection_task_for.sub_area.is_valid_area(checkin.latitude, checkin.longitude) and collection_task_for.time_restriction.is_valid_time(
                            checkin.datetime) and not collection_task_for.completed:
                    collection_task = collection_task_for
                    collection_task.completed = True
                    collection_task.save()
                    score_task_type = (ScoreAllocationStrategy.objects.filter(project_id=checkin.project.id, checkin=False,
                                                                              task_type=task_type.values()[0]['id']).values())
                    score_time_restriction = (ScoreAllocationStrategy.objects.filter(project_id=checkin.project.id, checkin=False,
                                                                              time_restriction=collection_task_for.time_restriction).values())
                    score_sub_area = (ScoreAllocationStrategy.objects.filter(project_id=checkin.project.id, checkin=False,
                                                                              sub_area=collection_task_for.sub_area).values())
                    points = score_task_type[0]['points'] + score_time_restriction[0]['points'] + score_sub_area[0]['points']
                    game_profile.set_participation(project[0], points)
                    game_profile.save()
        else:
            score = ScoreAllocationStrategy.objects.filter(project_id=checkin.project.id, checkin=True).values()
            points = score[0]['points']
            game_profile.set_participation(project[0], points)
            game_profile.save()
        game_move = GameMove.objects.create(points=points, checkin=checkin, game_profile=game_profile, collection_task=collection_task, badge=badge)

        if Competition.objects.filter(game_profile=game_profile, project=project[0]):
            competition = Competition.objects.get(game_profile=game_profile, project=project[0])
        else:
            competition = Competition.objects.create(game_profile=game_profile, project=project[0])
        competition.update_total_points(points)
        competition.save()

        return game_move

class GameProfileSerializer(serializers.ModelSerializer):

    user = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='username'
     )

    class Meta:
        model = GameProfile
        fields = '__all__'

class CompetitionSerializer(serializers.ModelSerializer):

    game_profile = GameProfileSerializer(many=False, read_only=True)

    class Meta:
        model = Competition
        fields = '__all__'
