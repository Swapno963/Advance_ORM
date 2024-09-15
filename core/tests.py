from django.test import TestCase
from .models import Resturent
# Create your tests here.

class ResturentTests(TestCase):
    def test_resturent_name_property(self):
        resturent = Resturent(name="test")
        self.assertEqual(resturent.resturent_name,'test')
        
        
        resturent.nickname = "klkdlfk"
        self.assertEqual(resturent.resturent_name,'klkdlfk')