from django.test import TestCase, Client
from django.urls import reverse, resolve
from katalog.models import CatalogItem
from katalog.views import show_katalog


class KatalogTest(TestCase):
    def test_create_katalog(self):
        CatalogItem.objects.create(
            item_name = "Ipad Pro", 
            item_price = 11000000, 
            item_stock = 1, 
            description = "11 inci 120 Hz", 
            rating = 4, 
            item_url = "https://ibox.co.id/catalogsearch/ipad+pro"
        )
        ipad = CatalogItem.objects.get(item_name="Ipad Pro")
        self.assertEquals(ipad.item_name, "Ipad Pro")

    def test_url_routing(self):
        url = reverse("katalog:show_katalog")
        self.assertEquals(resolve(url).func, show_katalog)

    def test_view_respond(self):
        client = Client()
        response = client.get(reverse("katalog:show_katalog"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "katalog.html")