from django.test import TestCase
from .models import *
import unittest

class TestProfile(TestCase):
    def setUp(self):
        self.user = User(id=1, username='kwash', password='kwamboka')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()


if __name__ == '__main__':
    unittest.main()  