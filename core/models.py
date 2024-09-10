from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.db.models.functions import Lower

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
        FASTFOOD = 'FD', 'FastFood'
        OTHER = 'OT', 'Other'
        
        
    name  = models.CharField(max_length=100,validators=[validate_resturent_name_begins_with_a])
    website = models.URLField(default="")
    date_opened = models.DateField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    resturent_type = models.CharField(max_length=2,choices=TypeChoces.choices)
    
    class Meta:
        ordering = [Lower('name')] # if we don't tell how to order then this is going to be default order
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs): # if we want to do some task besed one one obj created first time
        print(self._state.adding)
        super().save(*args, **kwargs)
    
class Staff(models.Model):
    name =models.CharField(max_length=128)
    resturent = models.ManyToManyField(Resturent, through="StaffResturent")
    
    def __str__(self):
        return self.name
    
    
class StaffResturent(models.Model):
    staff = models.ForeignKey(Staff,on_delete=models.CASCADE)
    resturent = models.ForeignKey(Resturent, on_delete=models.CASCADE)
    salary = models.FloatField(null=True)
    
    def __str__(self):
        return self.salary
    
    
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
    expenditure = models.DecimalField(max_digits=8, decimal_places=2)
    date_time = models.DateTimeField()
    
    def __str__(self):
        return f"Income: {self.income} expenditure: {self.expenditure}"
    
    
    
    
    
    
    
    
    
    
    
    
    
    