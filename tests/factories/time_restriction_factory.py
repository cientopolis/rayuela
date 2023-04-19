import factory
from datetime import datetime
import pytz
from alaapp.models.time_restriction import TimeRestriction

class TimeRestrictionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TimeRestriction
        django_get_or_create = ('name','date_from',)

    name='test_tr'
    date_from=datetime(2022, 10, 12, tzinfo=pytz.UTC)
    date_to=datetime(2022, 11, 12, tzinfo=pytz.UTC)
    hour_from='00:00'
    hour_to='23:59'

    @factory.post_generation
    def days(self, create, days):
        if not create:
            return

        if days:
            for day in days:
                self.days.add(day)

class OtherTimeRestrictionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TimeRestriction
    
    name='other_test_tr'
    date_from=datetime(2022, 8, 7, tzinfo=pytz.UTC)
    date_to=datetime(2022, 9, 7, tzinfo=pytz.UTC)
    hour_from='16:00'
    hour_to='23:59'
   