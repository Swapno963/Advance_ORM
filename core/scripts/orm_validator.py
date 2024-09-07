from core.models import Resturent,Rating,Sale
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User
from pprint import pprint

def run():
    user = User.objects.first()
    resturent = Resturent.objects.last()
    
    rating = Rating.objects.create(user=user,resturent=resturent, rating=9)
    rating.full_clean()
    rating.save()
    
    
    # pprint(connection.queries)