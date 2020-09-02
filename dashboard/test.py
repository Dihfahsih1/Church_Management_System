from django.test import TestCase
from dashboard.models import Testing
class WebsiteTests(TestCase):
    def test_page_is_created_successfully(self):
        page = Testing(
            name='Home',
            slug='home'
        )
        page.save()