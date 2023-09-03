import factory

from rayuelaApp.models.user import Role

class RoleAdminFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Role
        
    name='Admin'

class RolePlayerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Role
        
    name='Player'