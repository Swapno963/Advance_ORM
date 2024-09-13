from core.models import Resturent,Rating,Sale,Staff,StaffResturent
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User
from pprint import pprint
from django.db.models.functions import Lower,Upper,Length,Concat,Coalesce
import random
import itertools
from django.db.models import Count,Avg,Min,Max,Value,CharField,Sum,F,Q,Case,When,Subquery,OuterRef
def c_print(*args, **kwargs):
    print("\n", end="")

    print(*args, **kwargs)

    print("\n", end="")

def run():  
    # want to see sells of chinis and itelian resturent
    # sales = Sale.objects.filter(resturent__resturent_type__in=['IT','CH'])
    # print(sales.values('resturent__resturent_type'))
    
    
    # lets do it by subquery
    # resturent = Resturent.objects.filter(resturent_type__in=['IT','CH'])
    # sales = Sale.objects.filter(resturent__in=Subquery(resturent.values('pk')))
    # print(sales)
    
    
    # get most recent sale
    # resturents = Resturent.objects.all()
    # sales = Sale.objects.filter(resturent=OuterRef('pk')).order_by('-date_time')
    
    
    # resturents = resturents.annotate(
    #     last_sale_income = Subquery(sales.values("income")[:1])
    # )
    
    # for r in resturents:
    #     print(f"{r.pk}-{r.last_sale_income}")
    # print(sales)
    
    
    
    #  for each post, we’re fetching the latest comment using a subquery. This saves you from running a separate query for each post to get its latest comment. z
# class Post(models.Model):
#     title = models.CharField(max_length=200)
#     content = models.TextField()

# class Comment(models.Model):
#     post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
#     text = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
    
# from django.db.models import Subquery, OuterRef

# latest_comment = Comment.objects.filter(post=OuterRef('pk')).order_by('-created_at').values('text')[:1]

# posts = Post.objects.annotate(latest_comment=Subquery(latest_comment))

    
    
    
    
    
    
# OuterRef allows references to fields from the outer query inside a subquery. It’s typically used in conjunction with Subquery to compare fields from the main query with fields in the subquery.

# Real-World Example:
# You have an e-commerce application, and you want to get the most recent order date for each customer. The Order model refers to the customer through a foreign key, and you need the order date for each customer.
    
    
    
    
# class Customer(models.Model):
#     name = models.CharField(max_length=100)

# class Order(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     order_date = models.DateTimeField()

    
    
# from django.db.models import Subquery, OuterRef

# recent_order = Order.objects.filter(customer=OuterRef('pk')).order_by('-order_date').values('order_date')[:1]

# customers = Customer.objects.annotate(last_order_date=Subquery(recent_order))

    
    
    
        
        
        
        
        
#         Exists
# Exists is used to check whether a subquery returns any results. It returns a boolean value (True or False) based on whether the related data exists. This is particularly useful for optimizing queries when you only need to check the existence of related data, without fetching the actual data.

# Real-World Example:
# Imagine you have a job application system, and you want to find out which jobs have received at least one application.
        
        
        
# class Job(models.Model):
#     title = models.CharField(max_length=200)

# class Application(models.Model):
#     job = models.ForeignKey(Job, on_delete=models.CASCADE)
#     applicant_name = models.CharField(max_length=100)
        
        
        
# from django.db.models import Exists, OuterRef

# applications = Application.objects.filter(job=OuterRef('pk'))
# jobs_with_applications = Job.objects.annotate(has_applications=Exists(applications)).filter(has_applications=True)
        
        
        
        
        
        
#     Summary of Real-World Use Cases:
# Subquery: Retrieve related data (like the latest comment for each post) in a single query.
# OuterRef: Reference the outer query’s fields (like the customer pk) within a subquery to find related data.
# Exists: Efficiently check if related data exists (like whether a job has any applications).
        
        
        
        
        
    pprint(connection.queries)