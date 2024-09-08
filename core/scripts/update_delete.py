from core.models import Resturent,Rating,Sale
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User
from pprint import pprint

def run():
    # user = User.objects.first()
    # resturent = Resturent.objects.last()
    
    # print(resturent.name)
    # resturent.name = 'changeing name' 
    # resturent.save() # this will not only update the name but alose all the field
    
    
    # if we want to just update a specific field then 
    # resturent.name = 'changeing name 3'
    # resturent.save(update_fields=['name'])
    
    # we want to know wheather this model created or other(update)
    # Resturent.objects.create(
    #     name = "other GREEK resturent",
    #     latitude = 37.4,
    #     longitude = 55.8,
    #     date_opened = timezone.now(),
    #     resturent_type = Resturent.TypeChoces.GREEK
    # )
    
    
    # we want to update every single row
    resturents = Resturent.objects.all()
    resturents.update( # this is have a problem: by default if will not run save method or any pre or post save singnals
        date_opened = timezone.now()
    )
    pprint(connection.queries)
    