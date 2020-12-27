from django.test import SimpleTestCase
from django.urls import reverse, resolve

from contact.views import ContactView
from weapon.views import WeaponDetailView, CountryView, FilterWeaponView, JsonFilterMoviesView, \
     Search


class TestUrls(SimpleTestCase):

    def test_list_url_resolves(self):
        url = reverse("weapon_detail", args=['some-slug'])
        self.assertEquals(resolve(url).func.view_class, WeaponDetailView)

    def test_filter_url_resolves(self):
        url = reverse("filter")
        self.assertEquals(resolve(url).func.view_class, FilterWeaponView)

    def test_search_url_resolves(self):
        url = reverse("search")
        self.assertEquals(resolve(url).func.view_class, Search)

    def test_contact_url_resolves(self):
        url = reverse("contact")
        self.assertEquals(resolve(url).func.view_class, ContactView)

    def test_country_url_resolves(self):
        url = reverse("country_detail", args=['some-slug'])
        self.assertEquals(resolve(url).func.view_class, CountryView)

    def test_json_url_resolves(self):
        url = reverse("json_filter")
        self.assertEquals(resolve(url).func.view_class, JsonFilterMoviesView)

    def test_detail_url_resolves(self):
        url = reverse("weapon_detail", args=['some-slug'])
        self.assertEquals(resolve(url).func.view_class, WeaponDetailView)



