from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated

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


class JoinDisjoinTheProjectViewSet(viewsets.ModelViewSet):
    """Envío de parametros en PATCH \n
    ?project_id=number_id&join=bool
    'True' si se está uniendo y 'False' si lo está abandonando
    """
    serializer_class = VolunteerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Volunteer.objects.filter(username=user)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"project_id": self.request.query_params.get('project_id', 0),
                        "join": self.request.query_params.get('join', False)})
        return context


class ProjectsViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = () # Al estar vacío no se necesita permiso para acceder a esta vista

    queryset = Project.objects.filter(available=True)


class ProjectsWithoutTheUserViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        user_projects = user.projects
        projects = Project.objects.filter(available=True)
        return set(projects) ^ set(user_projects.all())


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
