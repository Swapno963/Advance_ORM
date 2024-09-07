from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Resturent(models.Model):
    class TypeChoces(models.TextChoices):
        INDIAN = 'IN', 'Indian'
        CHINESE = 'CH', 'Chinise'
        ITALIAN = 'IT', 'Italian'
        GREEK = 'GR', 'GREEK'
        MEXICAN = 'MD', 'Mexican'
        OTHER = 'OT', 'Other'
        
        
    name  = models.CharField(max_length=100)
    website = models.URLField(default="")
    date_opened = models.DateField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    resturent_type = models.CharField(max_length=2,choices=TypeChoces.choices)
    
    def __str__(self):
        return self.name
    
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resturent = models.ForeignKey(Resturent, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    
    def __str__(self):
        return f"Rating: {self.rating}"
    
    
    
    
class Sale(models.Model):
    resturent = models.ForeignKey(Resturent, on_delete=models.CASCADE, null=True)
    income = models.DecimalField(max_digits=8, decimal_places=2)
    date_time = models.DateTimeField()
    
    
    
    
    
    
    
    
    
    
    
    
    
    