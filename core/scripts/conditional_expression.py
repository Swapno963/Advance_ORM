from core.models import Resturent,Rating,Sale,Staff,StaffResturent
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User
from pprint import pprint
from django.db.models.functions import Lower,Upper,Length,Concat,Coalesce
import random
import itertools
from django.db.models import Count,Avg,Min,Max,Value,CharField,Sum,F,Q,Case,When
def c_print(*args, **kwargs):
    print("\n", end="")

    print(*args, **kwargs)

    print("\n", end="")

def run():  
    
    # 
    # italian = Resturent.TypeChoces.ITALIAN
    # resturent = Resturent.objects.annotate(
    #     is_italian=Case( # This will give true where resturent_tykkpe is italian
    #         When(resturent_type=italian, then=True),
    #         default=False
    #     )
    # )   
    # c_print(resturent.filter(is_italian=True))    
    # let see how many sells each resturent have
    # print(
    #     Resturent.objects.annotate(nsales=Count('sales')).values("nsales")
    #     )
    
    
    # get resturents whos have more then 8 sells
    # resturnets = Resturent.objects.annotate(nsales=Count('sales'))
    
    # resturents = resturnets.annotate(
    #     is_popular=Case(
    #         When(nsales__gt=8, then=True),
    #     default=False
    #     )
    # )
    # c_print(resturents.values('nsales','is_popular'))
    # print(resturents.filter(is_popular=True))
    
    
    
    
    # Resturent average rating > 3.5
    # Resturent has mroe than 1 rating
    
    # by this we can see the average rating and how many rating a resturent have
    # resturents = Resturent.objects.annotate(
    #     avg_rating = Avg('ratings__rating'),
    #     rating_num = Count('ratings__pk')
    # )
    # c_print(resturents.values('avg_rating','rating_count'))
    
    
    # Working with case wand where
    # resturents = resturents.annotate(
    #     follow_conditon = Case(
    #         When(avg_rating__gte=3.5,rating_num__gt=1, then=True),
    #         default=False
    #     )
    #   ,
    #     rating_count = Count('ratings')
    # )
    # c_print(resturents.filter(follow_conditon=True))

 
 
    
    # now we need 3 category of resturent 
    # resturents = resturents.annotate(
    #     rating_bucket = Case(
    #         When(avg_rating__gte=3.5, then=Value("Highly Rated")),
    #         When(avg_rating__range=(2.5,3.5), then=Value("Average Rated")),
    #         When(avg_rating__lt=2.5, then=Value("Bad Rated")),
    #     )
    # )
    # c_print(resturents.values('rating_bucket'))

    
    
    
    
    # assign a continect to each resturent
    # types = Resturent.TypeChoces
    # resturents = Resturent.objects.annotate(
    #     continent = Case(
    #         When(
    #             Q(resturent_type = types.INDIAN) | Q(resturent_type = types.CHINESE), then= Value("Asian")
    #             ),
    #         When(
    #             Q(resturent_type = types.ITALIAN) | Q(resturent_type = types.GREEK), then= Value("Europe")
    #             ),
    #         When(
    #             Q(resturent_type = types.MEXICAN) , then= Value("America")
    #             )
    #         )
    # ) 
    
    # c_print(resturents.values('continent'))
    
    
    
    
    
    # aggregating total sales over each 10 days period, startin from the first sale up untill the last
    # 1-10th
    # 11th-20th
    # 21th-30th
    
    # lets find out first and lase sale
    first_sale = Sale.objects.aggregate(first_sale_date=Min("date_time"))['first_sale_date']
    last_sale = Sale.objects.aggregate(lsst_sale_date=Max("date_time"))['lsst_sale_date']
    
    
    # generate a list of dates, each 10 days
    dates = []
    count = itertools.count()
    while (dt:=first_sale + timezone.timedelta(10*next(count))) <= last_sale:
        dates.append(dt)
    # print(dates)
    
    whens = [
        When(date_time__range=(dt, dt+timezone.timedelta(days=10)), then=Value(dt.date()))
        for dt in dates
    ]
    
    
    case = Case(
        *whens,
        output_field=CharField()
    )
    
    c_print(
        Sale.objects.annotate(
            daterange=case
        ).values('daterange').annotate(total_sales=Sum('income'))
    )
  
    
    
    
    
    
    
    
    
    
    
    
    
        
    pprint(connection.queries)