from core.models import Resturent,Rating,Sale,Staff,StaffResturent
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User
from pprint import pprint
from django.db.models.functions import Lower
import random
def run():
    # staff, created = Staff.objects.get_or_create(name="jon wicks")
    # print(staff.resturent.all())
    # staff.resturent.add(Resturent.objects.first()) # adding first resturent 
    # staff.resturent.remove(Resturent.objects.first()) 
    
    # this jon will work first five resturent
    # staff.resturent.set(Resturent.objects.all()[:15]) # adding first resturent 


    # remove jon from all resturent
    # staff.resturent.clear()
    
    
    # want to get itaian resturent where our stuf works
    # italian = staff.resturent.filter(resturent_type=Resturent.TypeChoces.ITALIAN)
    # print('Our italian stuf is :', italian)
    # print(staff.resturent.all())
    
    # get all stuff of a resturent
    # resturant = Resturent.objects.get(pk=33)
    # print(resturant.staff_set.all())
    
    # working with stffResturent
    staff, created = Staff.objects.get_or_create(name="jon wicks")
    resturent = Resturent.objects.first()
    resturent2 = Resturent.objects.last()
    
    # creating 2 row
    # StaffResturent.objects.create(
    #     staff=staff, resturent=resturent,salary=28_000
    # )
    # StaffResturent.objects.create(
    #     staff=staff, resturent=resturent2,salary=22_000
    # )
    
    
    
    # showing salary and rusturent for that staaf
    # staff_resturant = StaffResturent.objects.filter(staff=staff)
    # for s in staff_resturant:
    #     print(s.resturent)
    
    # remove all stafResturnt
    staff.resturent.clear()
    
    
    # association resturent and staff without salary
    # resturnt = Resturent.objects.first()
    # staff.resturent.add(resturnt)
    
    
    # add salary
    # staff.resturent.add(resturent, through_defaults={'salary':5000})
    
    
    # add 15 rows
    staff.resturent.set(
        Resturent.objects.all()[:15], 
        through_defaults={'salary': random.randint(20_000,80_000)}
        )