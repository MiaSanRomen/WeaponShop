from django.test import TestCase
from weapon.models import Weapon


class TestModels(TestCase):

    def setUp(self):
        self.project1 = Weapon.objects.create(
            name='weapon',
            description='test',
            price=5000,
        )

    def test_wine_is_assigned_slug_on_getting(self):
        self.assertEquals(self.project1.url, self.project1.url)
