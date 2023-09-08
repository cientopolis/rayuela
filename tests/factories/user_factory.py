import factory

from rayuelaApp.models.user import User
from werkzeug.security import generate_password_hash
from tests.factories.role_factory import RoleAdminFactory, RolePlayerFactory


class UserAdminFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    id=1
    complete_name='admin_test'
    username='admin_test'
    email='testadmin@gmail.com'
    password=generate_password_hash('12345', 'sha256', 10)
    role_id=factory.SubFactory(RoleAdminFactory)


class UserPlayerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username','email',)
    id=2
    complete_name='player_test'
    username='player_test'
    email='testplayer@gmail.com'
    password=generate_password_hash('12345', 'sha256', 10)
    role_id=factory.SubFactory(RolePlayerFactory)

