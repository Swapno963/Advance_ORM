from core.models import Resturent,Rating,Sale,Staff,StaffResturent
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User
from pprint import pprint
from django.db.models.functions import Lower,Upper,Length,Concat
import random
from django.db.models import Count,Avg,Min,Max,Value,CharField,Sum
def c_print(*args, **kwargs):
    print("\n", end="")

    print(*args, **kwargs)

    print("\n", end="")

def run():
    # print("\n")     
    # getting all the  resturent 
    # resturent = Resturent.objects.all()
    
    # if we want jus name and date then we can use value to get dictionary rather then model
    # resturent = Resturent.objects.values('name','date_opened')
    # print(resturent)
    
    # we want resturen in uppercase
    # resturent = Resturent.objects.values(name_upper=Upper('name'))
    # c_print(resturent)
    
        # if we want jus name and date then we can use value to get tuple rather then model
    # resturent = Resturent.objects.values_list('name','date_opened')
    
    # to remove tuple
    # resturent = Resturent.objects.values_list('name', flat=True)



    # what to know how many resturent start with 'c'
    # c_print(Resturent.objects.filter(name__startswith='c').count())
    
    # want to know how many data we have
    # c_print(Resturent.objects.aggregate(Count('id')))
    
    
    # avg, min and max rating
    # c_print(Rating.objects.filter(resturent__name__startswith='c').aggregate(
    #     avg=Avg('rating'),
    #     min=Min('rating'),
    #     max=Max('rating')
    #     ))
    
    # get neme and length of name in resturent
    # resturent = Resturent.objects.annotate(len_name=Length('name'))
    # c_print(resturent.values('name','len_name'))
    
    # we want onlwy those whose name length is more then 5
    # resturent = Resturent.objects.annotate(len_name=Length('name')).filter(
    #         len_name__gte=10
    #     )
    # c_print(resturent.values('name','len_name'))
    
    
    
    # nwo we want to show a resturent name and it's average rating
    # concatination = Concat(
    #     'name',Value('[rating: '), Avg('ratings__rating'), Value(']'),
    #     output_field=CharField()
    # )
    
    # resturent = Resturent.objects.annotate(message=concatination)
    # for r in resturent:
    #     print(r.message)
    
    
    # get resturent name and how many rating that resturen have
    # resturent = Resturent.objects.annotate(
    #     total_rating=Count("ratings"),
    #     avg_rating=Avg('ratings__rating')
    #     )
    # c_print(resturent.values('name','total_rating','avg_rating'))
    
    
    # how many rating have of diffrent type of resutent
    # resturent = Resturent.objects.values('resturent_type').annotate(
    #     num_rating = Count('ratings')
    # )
    # c_print(resturent)
    
    
    # seles incom
    # resturent = Resturent.objects.annotate(total_sale=Sum("sales__income"))
    # for r in resturent:
    #     c_print(r.total_sale)  # hear order heapping by resturen id
        
    # now we want to order it by total sale
    # resturent = Resturent.objects.annotate(total_sale=Sum("sales__income")).order_by('total_sale')
    # for r in resturent:
    #     print(r.total_sale)  # hear order heapping by resturen id
        
    
    # nwo we want to see only those sale that have more then 300
    resturent = Resturent.objects.annotate(total_sale=Sum("sales__income")).filter(total_sale__gt=300).order_by('total_sale')
    for r in resturent:
        print(r.total_sale)  # hear order heapping by resturen id
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # print("\n") 
    pprint(connection.queries)
    # print("\n") 