from core.models import Resturent,Rating,Sale,Staff,StaffResturent,Task,TaskStatus,InProgressTask
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
    sale = Sale.objects.first()
    sale.income = 10
    sale.save()
    # print(sale)
    # print(sale.profit)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
    
    
    pprint(connection.queries)