from django.shortcuts import render
from .models import Resturent,Rating,Sale
from django.db.models import Sum,Prefetch
from django.utils import timezone

# Create your views here.
def index(request):
    # resturents = Resturent.objects.all() #This is not efficient
    resturents = Resturent.objects.filter(name__istartswith='c').prefetch_related("ratings","sales") #this is most optimized way
    context = { 'resturents':resturents}
    return render(request, 'index.html',context)

def rating(request):
    # rating = Rating.objects.all()  #this is most optimized way, thsi will first bring rating then query again and again for resturent and user
    
    # rating = Rating.objects.select_related("resturent","user") #this is most optimized way, we are telling with rating we need resturenet  nad user
    
    # pro optimization : previous one brings all of colum, we can optimize even more by bring only those we need
    rating = Rating.objects.only("rating","resturent__name","user__email").select_related("resturent","user") 
    context = { 'ratings':rating}
    return render(request, 'rating.html',context)


def fiveStar(request):
    # get all 5 star ratings, and fetch all the sales for restaurants with 5 star ratings
    total_moeny = Resturent.objects.prefetch_related("ratings","sales")  \
        .filter(ratings__rating=5) \
        .annotate(total=Sum('sales__income'))
    print("Total money is:",total_moeny)
    # context = { 'ratings':rating} 
    # return render(request, 'rating.html')


def fiveStar_again(request):
    # get all 5 star ratings, and fetch all the sales for restaurants with 5 star ratings
    month_ago = timezone.now() - timezone.timedelta(days=30)
    monthly_sales = Prefetch(
        'sales',
        queryset=Sale.objects.filter(date_time__gte=month_ago)
    )
    resturent = Resturent.objects.prefetch_related("ratings",monthly_sales)  \
        .filter(ratings__rating=5) 
        
    total_money = resturent.annotate(total=Sum('sales__income'))
        # \
        # .annotate(total=Sum('sales__income'))
    print("resturnt:",resturent,' total_money',total_money)
    # context = { 'ratings':rating} 