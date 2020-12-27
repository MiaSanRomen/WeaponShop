from django.test import TestCase, Client
from django.urls import reverse
from weapon.models import Weapon, WeaponType, Category, Bullets, Reviews, Rating, RatingStar, Country

import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.detail_url = reverse("weapon_detail", args=['project1'])
        self.add_rating = reverse("add_rating")
        self.country_detail = reverse("country_detail", args=['project1'])
        self.project1 = Weapon.objects.create(
            name="project1",
            description="test",
            price=5000,
            image="grape",
            url="project1"
        )

    def test_weapon_detail_get(self):
        response = self.client.get(self.detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'weapon/weapon_detail.html')
