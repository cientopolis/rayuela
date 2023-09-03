import factory
import datetime

from rayuelaApp.models.check_in import CheckIn

from tests.factories.user_factory import UserPlayerFactory
from tests.factories.project_factory import ProjectFactory

class CheckinFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CheckIn

    
    user=factory.SubFactory(UserPlayerFactory)
    project=factory.SubFactory(ProjectFactory)
    latitude='-34.90972222'
    longitude='-57.93361111'
    datetime= '2022-10-20 15:26:10'

class InvalidCheckinFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CheckIn

    
    user=factory.SubFactory(UserPlayerFactory)
    project=factory.SubFactory(ProjectFactory)
    latitude='-42'
    longitude='-66'
    datetime= '2022-10-01 11:21:37'