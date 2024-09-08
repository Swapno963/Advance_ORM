from core.models import Resturent,Rating,Sale
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User
from pprint import pprint
from django.db.models.functions import Lower
def run():
    # chinese = Resturent.TypeChoces.CHINESE
    # resturent = Resturent.objects.filter(resturent_type=chinese, name__startswith="c") # this works like "and" in sql 
    # print(resturent)
    
    
    # if we have n number of lookup then
    # chinese = Resturent.TypeChoces.CHINESE
    # indian = Resturent.TypeChoces.INDIAN
    # fastFood = Resturent.TypeChoces.FASTFOOD
    # check_types = [chinese,indian, fastFood]
    # resturent = Resturent.objects.filter(resturent_type__in=check_types) # this works like "and" in sql 
    # print("N lookup: ", resturent)
    
    
    # order by name 
    # resturent = Resturent.objects.order_by('name')
    
    # order by name in a reverse way
    # resturent_re = Resturent.objects.order_by('-name')
    
    
    
    # those are case sensetive means they order capital letter first then small letter
    # for ordering case in-sensative
    # django allows to run db function while query, This lower function will execute at db layer
    # resturent = Resturent.objects.order_by(Lower('name'))
    # print(resturent)
    
    
    # let's work with join
    # we want rating of those resturent whose name starts with 'c'
    # rating = Rating.objects.filter(resturent__name__startswith="c")
    # print(rating)
    
    # all sels belongs to chinise resturent
    chinese = Resturent.TypeChoces.CHINESE
    sales = Sale.objects.filter(resturent__resturent_type=chinese)
    print(sales)
    pprint(connection.queries)