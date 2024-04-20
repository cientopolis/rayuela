from rest_framework import status, viewsets

from users.models import Volunteer, RayuelaUser
from rayuelaApp.models.project import Project

from rayuelaApp.api.serializers import RayuelaUserSerializer
from rayuelaApp.api.serializers import VolunteerSerializer
from rayuelaApp.api.serializers import ProjectSerializer

class RayuelaUserViewSet(viewsets.ModelViewSet):
    serializer_class = RayuelaUserSerializer
    queryset = RayuelaUser.objects.all()

class LoginViewSet(viewsets.ModelViewSet):
    serializer_class = VolunteerSerializer

    def get_queryset(self):
        user = self.request.user
        return Volunteer.objects.filter(username=user)

    #queryset = Volunteer.objects.all()
    permission_classes = () # Al estar vacío no se necesita permiso para acceder a esta vista

# class LoginViewSet(viewsets.ModelViewSet):
#     serializer_class = VolunteerSerializer
#     queryset = Volunteer.objects.all()

class LogoutViewSet(viewsets.ModelViewSet):
    serializer_class = VolunteerSerializer
    queryset = Volunteer.objects.all()

class RegisterViewSet(viewsets.ModelViewSet):
    serializer_class = VolunteerSerializer
    permission_classes = ()  # Al estar vacío no se necesita permiso para acceder a esta vista
    #queryset = Volunteer.objects.all()

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    # authentication_classes = () # Al estar vacío no se necesita autenticación para acceder a esta vista
    permission_classes = () # Al estar vacío no se necesita permiso para acceder a esta vista
    queryset = Project.objects.filter(available=True)
