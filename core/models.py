from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
# custom validator
def validate_resturent_name_begins_with_a(value):
    if not value.startwith("a"):
        raise ValidationError("resturent name must begin with 'a'")

# Create your models here.
class Resturent(models.Model):
    class TypeChoces(models.TextChoices):
        INDIAN = 'IN', 'Indian'
        CHINESE = 'CH', 'Chinise'
        ITALIAN = 'IT', 'Italian'
        GREEK = 'GR', 'GREEK'
        MEXICAN = 'MD', 'Mexican'
        OTHER = 'OT', 'Other'
        
        
    name  = models.CharField(max_length=100,validators=[validate_resturent_name_begins_with_a])
    website = models.URLField(default="")
    date_opened = models.DateField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    resturent_type = models.CharField(max_length=2,choices=TypeChoces.choices)
    
    def __str__(self):
        return self.name
    
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resturent = models.ForeignKey(Resturent, on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(5)]
    )
    
    def __str__(self):
        return f"Rating: {self.rating}"
    
    
    
    
class Sale(models.Model):
    resturent = models.ForeignKey(Resturent, on_delete=models.CASCADE, null=True, related_name='sales')
    income = models.DecimalField(max_digits=8, decimal_places=2)
    date_time = models.DateTimeField()
    
    
    
    
    
    
    
    
    
    
    
    
    
    