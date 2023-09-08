import factory

from rayuelaApp.models.assignment import Assignment
from tests.factories.user_factory import UserPlayerFactory
from tests.factories.challenge_factory import ChallengeFactory

class AssignmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Assignment
        django_get_or_create = ('user','game_element')
    
    user=factory.SubFactory(UserPlayerFactory)
    game_element=factory.SubFactory(ChallengeFactory)

    



