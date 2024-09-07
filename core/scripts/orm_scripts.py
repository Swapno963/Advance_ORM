from core.models import Resturent,Rating,Sale
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User
from pprint import pprint

def run():
    # creating a new row of data
    # resturent = Resturent()
    # resturent.name = "your indian resturent"
    # resturent.latitude = 47.4
    # resturent.longitude = 65.8
    # resturent.date_opened = timezone.now()
    # resturent.resturent_type = Resturent.TypeChoces.INDIAN
    # resturent.save()
    
    # another way of creating data
    # Resturent.objects.create(
    #     name = "other indian resturent",
    #     latitude = 17.4,
    #     longitude = 65.8,
    #     date_opened = timezone.now(),
    #     resturent_type = Resturent.TypeChoces.INDIAN
    # )
    
    
    # get all object from resturent
    # resturents = Resturent.objects.all()
    # print(resturents)
    
    # get first object from resturent
    # resturents = Resturent.objects.first()
    # print("first resturnet",resturents)
    
    
    # working with foreign key
    # resturent = Resturent.objects.first()
    # user = User.objects.first()
    # Rating.objects.create(user=user,resturent=resturent,rating=1)
    
    
    # get all the rating
    # rating = Rating.objects.all()
    # print(rating)
    
    # the those rating greater then or equal to 3
    # print(Rating.objects.filter(rating__gte=3))
    
    
    # the those rating lesser then or equal to 3
    # print(Rating.objects.filter(rating__lte=3))
    
    # if we want all of those who don't match the conditon
    # print(Rating.objects.exclude(rating__lte=3))
    
    
    
    # change the name of first resturent name
    # resturent = Resturent.objects.first()
    # print(resturent.name)
    # resturent.name = "changed name"
    # resturent.save()
    
    
    # useing resturent name
    # rating = Rating.objects.first()
    # print(rating.resturent)
    
    # get all the rating of a resturent
    # resturent = Resturent.objects.first()
    # print(resturent.rating_set.all())
    
    # we can do the same thing by related name
    # resturent = Resturent.objects.first()
    # print(resturent.ratings.all())
    
    
    # creating some sales
    # Sale.objects.create(
    #     resturent=Resturent.objects.first(),
    #     income=2.34,
    #     date_time=timezone.now()
    # )
    
    
    # get or get rating
    user = User.objects.first()
    resturent = Resturent.objects.last()
    rating, created = Rating.objects.get_or_create(
        resturent=resturent,
        user=user,
        rating=1
    )
    
    if created:
        #send email
        pass

    
    
    pprint(connection.queries)