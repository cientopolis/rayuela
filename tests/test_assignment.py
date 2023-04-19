from django.test import TestCase

from tests.factories.assignment_factory import AssignmentFactory


class AssignmentTestCase(TestCase):

    def setUp(self):
        self.assignment=AssignmentFactory.create()
        
    def test_assignment_add_like(self):
        self.assertIsNone(self.assignment.get_like_dislike())
        self.assignment.add_like_dislike('true')
        self.assertTrue(self.assignment.get_like_dislike())

    def test_assignment_add_dislike(self):
        self.assertIsNone(self.assignment.get_like_dislike())
        self.assignment.add_like_dislike('false')
        self.assertFalse(self.assignment.get_like_dislike())

    def test_assignment_increment_progress(self):
        self.assertEqual(self.assignment.get_progress(),0)
        self.assignment.increment_progress(5,3)
        self.assertEqual(self.assignment.get_progress(),60)