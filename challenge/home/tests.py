from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class IndexViewTests(TestCase):
    def test_index_live(self):
        """
        We test if we are getting the correct reposnse when we visit the index view.
        """
        response = self.client.get(reverse('home:index'))
        self.assertEqual(response.status_code, 200)