from django.db import models
from django.contrib.auth.models import AbstractUser
from rayuelaApp.models.project import Project


# Clase global de todos los usuarios.
class RayuelaUser(AbstractUser):
    """
    Si hay un atributo en común para todos los usuarios se declara acá
    """
    profile_image = models.ImageField(upload_to='rayuelaApp/static/profile_image/', default='rayuelaApp/static/profile_image/user.png', null=False, blank=False)
    complete_name = models.CharField(max_length=30, blank=True, null=True)
    projects = models.ManyToManyField(Project, blank=True)

    REQUIRED_FIELDS = ['email', 'password']


# Perfil personas voluntarias
class Volunteer(RayuelaUser):

    class Meta:
        verbose_name = 'Persona voluntaria'
        verbose_name_plural = 'Personas voluntarias'

    def add_project(self, project):
        self.projects.add(project)
        self.save()
