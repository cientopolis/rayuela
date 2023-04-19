from django.test import TestCase
from tests.factories.project_factory import ProjectFactory
from tests.factories.user_factory import UserAdminFactory
from tests.factories.time_restriction_factory import TimeRestrictionFactory
from tests.factories.area_factory import ProjectAreaFactory

class ProjectTestCase(TestCase):

    def setUp(self):
        self.admin_user=UserAdminFactory.create()
        self.time_restriction=TimeRestrictionFactory.create()
        self.area=ProjectAreaFactory.create()
        self.first_project=ProjectFactory.create()

    
    def test_project_add_admin(self):
  
        self.assertFalse(self.first_project.is_my_admin(self.admin_user.get_id()))   
        self.first_project.add_admin(self.admin_user)       
        self.assertTrue(self.first_project.is_my_admin(self.admin_user.get_id()))  

    def test_project_add_time_restriction(self):
        self.assertFalse(self.first_project.is_my_time_restriction(self.time_restriction.get_id()))
        self.first_project.add_time_restriction(self.time_restriction)
        self.assertTrue(self.first_project.is_my_time_restriction(self.time_restriction.get_id()))

    def test_project_add_area(self):
        self.assertIsNone(self.first_project.get_area())
        self.first_project.add_area(self.area)
        self.assertEqual(self.first_project.get_area(),self.area)

    def test_project_change_avaliable(self):
        self.assertFalse(self.first_project.get_avaliable())   
        self.first_project.set_avaliable(True)
        self.assertTrue(self.first_project.get_avaliable())    
        