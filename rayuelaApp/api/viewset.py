from rest_framework import status, viewsets

from rayuelaApp.models.user import User
from rayuelaApp.models.project import Project

from rayuelaApp.api.serializers import UserSerializer
from rayuelaApp.api.serializers import ProjectSerializer

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.filter(available=True)
