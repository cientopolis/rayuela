from django.test import TestCase
from tests.factories.user_factory import UserAdminFactory,UserPlayerFactory
from tests.factories.project_factory import ProjectFactory


class UserTestCase(TestCase):

    def setUp(self):
        self.admin_user=UserAdminFactory.create()
        self.player_user=UserPlayerFactory.create()
        self.first_project=ProjectFactory.create()
        

    def test_admin_user_creation(self):         
        self.assertEqual(self.admin_user.get_complete_name(),'admin_test')

    def test_player_user_creation(self):
        self.assertEqual(self.player_user.get_complete_name(),'player_test')

    def test_player_suscribe_project(self):
        self.assertQuerysetEqual(self.player_user.get_projects(),[])
        self.player_user.add_project(self.first_project)
        self.assertQuerysetEqual(self.player_user.get_projects(),[self.first_project])

    def test_player_update(self):
        self.assertEqual(self.player_user.get_complete_name(),'player_test')
        self.assertEqual(self.player_user.get_email(),'testplayer@gmail.com')

        self.player_user.update_data('other_player_test','othertestplayer@gmail.com','34678')

        self.assertEqual(self.player_user.get_complete_name(),'other_player_test')
        self.assertEqual(self.player_user.get_email(),'othertestplayer@gmail.com')