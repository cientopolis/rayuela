from crypt import methods
from distutils.util import strtobool

#from drf_yasg.openapi import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from users.models import Volunteer
from rayuelaApp.models.project import Project
from rayuelaApp.models.check_in import CheckIn
from rayuelaApp.models.collection_task import CollectionTask
from rayuelaApp.api.serializers import VolunteerSerializer, ProjectSerializer, CheckinSerializer, \
    CollectionTaskSerializer


class LoginViewSet(viewsets.ModelViewSet):
    serializer_class = VolunteerSerializer
    permission_classes = () # Al estar vacío no se necesita permiso para acceder a esta vista

    def get_queryset(self):
        user = self.request.user
        return Volunteer.objects.filter(username=user)


class RegisterViewSet(viewsets.ModelViewSet):
    serializer_class = VolunteerSerializer
    permission_classes = ()  # Al estar vacío no se necesita permiso para acceder a esta vista


class VolunteerViewSet(viewsets.ModelViewSet):
    serializer_class = VolunteerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Volunteer.objects.filter(username=user)

    @action(detail=True, methods=['patch'])
    def join_or_disjoin_the_project(self, request, pk=None):
        """
        Necesita envío de parametros \n
        - project_id: number
        - join: bool
        - Parametros y valores en URL: ?project_id=number_id&join=bool
        """
        instance = self.get_object()
        project_id = self.request.query_params.get('project_id', 0)
        join = strtobool(self.request.query_params.get('join', False))
        if join:
            instance.projects.add(project_id)
        else:
            instance.projects.remove(project_id)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class ProjectsViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = () # Al estar vacío no se necesita permiso para acceder a esta vista

    queryset = Project.objects.filter(available=True)


class ProjectsWithoutTheUserViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        projects = Project.objects.filter(available=True)
        return set(projects) ^ set(user.projects.all())


class CheckinViewset(viewsets.ModelViewSet):
    """
    Necesita envío de parametro en GET{id} \n
    - project_id: number
    - Parametro y valor en URL: ?project_id=number_id
    """
    serializer_class = CheckinSerializer
    permission_classes = [IsAuthenticated]

    # Devuelve checkins de project y user actuales
    def get_queryset(self):
        user = self.request.user
        project = self.request.query_params.get('project_id', 0)
        return CheckIn.objects.filter(user=user.id, project=project)


class ProjectCollectionTasksViewSet(viewsets.ModelViewSet):
    serializer_class = CollectionTaskSerializer
    permission_classes = ()  # Al estar vacío no se necesita permiso para acceder a esta vista

    def get_queryset(self):
        tasks_project = []
        tasks = CollectionTask.objects.all()
        project = Project.objects.filter(available=True, id=self.request.query_params.get('project_id', 0))
        for task in tasks:
            for collection_task in project.values('collection_tasks'):
                if task.id == collection_task['collection_tasks']:
                    tasks_project.append(task)
        return tasks_project

class CollectionTaskViewSet(viewsets.ModelViewSet):
    serializer_class = CollectionTaskSerializer
    permission_classes = ()  # Al estar vacío no se necesita permiso para acceder a esta vista

    queryset = CollectionTask.objects.all()