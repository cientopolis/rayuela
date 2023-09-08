import factory


from rayuelaApp.models.day import Day

class MondayDayFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Day
        
    id=1
    name='Lunes'


class TuesdayDayFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Day
        
    id=2
    name='Martes'

class WednesdayDayFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Day
        
    id=3
    name='Miércoles'

class ThursdayDayFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Day
        
    id=4
    name='Jueves'

class FridayDayFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Day
        
    id=5
    name='Viernes'    

class SaturdayDayFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Day
        
    id=6
    name='Sabado'    

class SundayDayFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Day
        
    id=7
    name='Sabado'  