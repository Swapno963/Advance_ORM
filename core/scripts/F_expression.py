# It makes it possible to refer to model field values and perform database operations using them without actually having to pull them out of the database into Python memory.


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
    # rating = Rating.objects.filter(rating=3).first()
    # c_print(rating)
    # rating.rating += 1 #this need two query, one for geting the data and another is for updateing
    # rating.rating =F('rating') + 1 # done it's work by one query
    # rating.save()
    
    
    
    # To make double of rating
    # Rating.objects.update(rating=F('rating')/2) # by one query it will update each row of table
    
    
    # Now update all table
    # sales =Sale.objects.all()
    
    # for sale in sales:
    #     sale.expenditure = random.uniform(5,100)
        
    # Sale.objects.bulk_update(sales,['expenditure'])
    
    
    # get sells whose expenditure is greter then income
    # sales = Sale.objects.filter(expenditure__gt=F('income'))
    # print(sales)
    
    
    
    # know lose of first obj
    # sales = Sale.objects.annotate(
    #     profit=F('income')-F('expenditure')
    # )
    # print(sales.first().profit)
    
    # # know higest lose  obj
    # sales = Sale.objects.annotate(
    #     profit=F('income')-F('expenditure')
    # ).order_by('profit')
    # print(sales.first().profit)
    
    # # know higest profit of first obj
    # sales = Sale.objects.annotate(
    #     profit=F('income')-F('expenditure')
    # ).order_by('-profit')
    # print(sales.first().profit)
    
    
    
    
    
    # now we want to know how many times we make profit, lose
    # sales = Sale.objects.aggregate(
    #     profit = Count('id', filter=Q(income__gt=F('expenditure'))),
    #     lose = Count('id', filter=Q(income__lt=F('expenditure')))
    # ) 
    # print(sales)
    
    
    
    rating =Rating.objects.first()
    print(rating.rating)
    rating.rating = F('rating') + 1
    rating.save()
    print(rating.rating)     # F(rating) + Value(1)
    # to see the exctual valu
    rating.refresh_from_db()
    print(rating.rating)     
     
    
    
    
    
    
    
    
    
    
    
    
    
    pprint(connection.queries)