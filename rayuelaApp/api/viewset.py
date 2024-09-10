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
from rayuelaApp.api.serializers import VolunteerSerializer, ProjectSerializer, CheckinSerializer


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
    Envío de parametro en GET \n
    ?project_id=number_id
    """
    serializer_class = CheckinSerializer
    permission_classes = [IsAuthenticated]

    # Devuelve checkins de project y user actuales
    def get_queryset(self):
        user = self.request.user
        project = self.request.query_params.get('project_id', 0)
        return CheckIn.objects.filter(user=user.id, project=project)
