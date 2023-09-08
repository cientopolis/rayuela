
import factory

from rayuelaApp.models.challenge import Challenge
from tests.factories.project_factory import ProjectFactory

class ChallengeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Challenge
        django_get_or_create = ('name','project','goal')
    name='challenge_test'
    project=factory.SubFactory(ProjectFactory)
    goal=5





    