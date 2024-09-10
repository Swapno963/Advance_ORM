from core.models import Resturent,Rating,Sale,Staff,StaffResturent
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User
from pprint import pprint
from django.db.models.functions import Lower,Upper,Length,Concat
import random
from django.db.models import Count,Avg,Min,Max,Value,CharField,Sum,F,Q
def c_print(*args, **kwargs):
    print("\n", end="")

    print(*args, **kwargs)

    print("\n", end="")

def run():
    # it = Resturent.TypeChoces.ITALIAN
    # mex = Resturent.TypeChoces.ITALIAN
    # resturent = Resturent.objects.filter(
    #     Q(resturent_type=it) | Q(resturent_type=mex) # or condition
    # )
    # print(resturent)
    
    
    # want those resturent whose name contain italian and mexican and opend in last 40 days
    # it_or_mex = Q(name__icontains="italian") | Q(name__contains="mexican")
    # recently_opended = Q(date_opened__gt=timezone.now() - timezone.timedelta(days=40))
    # not_recently_opended = ~Q(date_opened__gt=timezone.now() - timezone.timedelta(days=40))
    # resturnet = Resturent.objects.filter(it_or_mex | not_recently_opended)
    # print(resturnet)
    
    
    
    # want to know does our name have any number or not, or lets check is it profiable
    # is_profiable = Q(income__gt=F('expenditure'))
    # name_has_num = Q(resturent__name__regex="[0-9]+")
    # name_with_num = Sale.objects.filter(name_has_num |is_profiable)
    # print(name_with_num)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    pprint(connection.queries)