from django.db import models
from django.contrib.auth.models import AbstractUser
from rayuelaApp.models.project import Project


# Clase global de todos los usuarios.
class RayuelaUser(AbstractUser):
    """
    Si hay un atributo en comun para todos los usuarios se declara aca
    """
    profile_image = models.ImageField(upload_to='rayuelaApp/static/profile_image/', default='rayuelaApp/static/profile_image/user.png', null=False, blank=False)
    complete_name = models.CharField(max_length=30, blank=True, null=True)
    projects = models.ManyToManyField(Project, blank=True)

    REQUIRED_FIELDS = ['email', 'password']

    # def save(self, *args, **kwargs):
    #     self.set_password(self.password)
    #     super().save(*args, **kwargs)


# Peril personas voluntarias
class Volunteer(RayuelaUser):

    class Meta:
        verbose_name = 'Persona voluntaria'
        verbose_name_plural = 'Personas voluntarias'

    # def __str__(self):
    #     return f'{self.complete_name},{self.username},{self.email},{self.password},{self.profile_image},{self.projects}'

    def add_project(self, project):
        self.projects.add(project)
        self.save()
