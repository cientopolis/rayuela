import factory

from alaapp.models.project import Project



class ProjectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Project
        django_get_or_create = ('name','description',)
    
    name='project_test'
    description='description_test'
    avaliable=False

