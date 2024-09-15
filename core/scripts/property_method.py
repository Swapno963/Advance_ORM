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
    # task = Task.objects.filter(status=TaskStatus.IN_PROGRESS)
    res = Resturent.objects.first()
    # c_print(res.resturent_name)
    # c_print(res.was_opened_this_year)
    
    now = timezone.now().date()
    reference_date = now - timezone.timedelta(days=5)
    print(res.is_opened_after(reference_date))
    
    # InProgressTask.objects.create(name="learning")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
    
    
    pprint(connection.queries)