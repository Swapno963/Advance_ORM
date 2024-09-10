from core.models import Resturent,Rating,Sale,Staff,StaffResturent
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User
from pprint import pprint
from django.db.models.functions import Lower,Upper,Length,Concat,Coalesce
import random
from django.db.models import Count,Avg,Min,Max,Value,CharField,Sum,F,Q
def c_print(*args, **kwargs):
    print("\n", end="")

    print(*args, **kwargs)

    print("\n", end="")

def run():    
    # get all the row whose value is null
    # c_print(Resturent.objects.filter(capacity__isnull=True))
    
    
    
    # we don't want null capacity
    # r1 = Resturent.objects.first()
    # r2 = Resturent.objects.last()
    # r1.capacity = 10
    # r2.capacity = 13
    # r1.save()
    # r2.save()
    
    # c_print(Resturent.objects.filter(capacity__isnull=False))
    
    
    
    
    # By default order by give null value first
    # c_print(Resturent.objects.order_by("capacity").values("capacity"))

    # To put nun value at the  last
    # c_print(Resturent.objects.order_by(F("capacity").asc(nulls_last=True)).values("capacity"))

    
    
    
    # to sum null values, this will give number 
    # c_print(Resturent.objects.aggregate(
    #     total_cap=Sum("capacity")
    # ))
    
    
    # if all the values are null then we need to handel it
    # c_print(Resturent.objects.aggregate(
    #     total_cap=Coalesce(Sum("capacity"),0)
    # ))
    
    
    # we though to work with nicknames but incase we don't have nickname then we give name
    c_print(
        Resturent.objects.annotate(
            name_value=Coalesce(F("nickname"), F('name'))
        ).values("name_value")
    )
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    pprint(connection.queries)