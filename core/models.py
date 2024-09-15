from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.db.models.functions import Lower
from django.db.models import Count,Avg,Min,Max,Value,CharField,Sum,F,Q,Case,When
from django.utils import timezone
from datetime import date
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
    capacity = models.PositiveIntegerField(null=True, blank=True)
    nickname = models.CharField(max_length=200, default="")
    
    
    @property
    def resturent_name(self):
        return self.nickname or self.name
    
    @property
    def was_opened_this_year(self) ->bool:
        current_year = timezone.now().year
        return self.date_opened.year == current_year
    
    # method
    def is_opened_after(self, date:date) ->bool:
        return self.date_opened > date
    
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
    
    class Meta:
        constraints = [
            models.CheckConstraint(
            name="raing_value_valid",
            check=Q(rating__gte=1, rating__lte=5),
            violation_error_message="Rataing invalid: Must fall between 1 and 5."
            )
   
        ]
    
    
class Sale(models.Model):
    resturent = models.ForeignKey(Resturent, on_delete=models.CASCADE, null=True, related_name='sales')
    income = models.DecimalField(max_digits=8, decimal_places=2)
    expenditure = models.DecimalField(max_digits=8, decimal_places=2)
    date_time = models.DateTimeField()
    
    profit = models.GeneratedField(
        expression = models.F('income') - models.F("expenditure"),
        output_field=models.DecimalField(max_digits=5, decimal_places=2),
        db_persist=True
    )
    
    # conditionaly set tip
    suggested_tip = models.GeneratedField(
        expression=Case(
            When(income__gte=10, then=models.F('income') * 0.2),
            default=Value(0),
            output_field=models.DecimalField(max_digits=5, decimal_places=2),
        ),
            output_field=models.DecimalField(max_digits=5, decimal_places=2),
            db_persist=True
    )
    
    
    def __str__(self):
        return f"Income: {self.income} expenditure: {self.expenditure}"
    
 
 

class Package(models.Model):
    DURATION_CHOICES = (
        (3, '3 Days'),
        (7, '7 Days'),
        (15, '15 Days'),
        (30, '30 Days'),
    )

    TYPE_CHOICES = (
        ('Regular', 'Regular'),
        ('Premium', 'Premium'),
    )

    plan = models.IntegerField(choices=DURATION_CHOICES)
    type = models.CharField(max_length=30, choices=TYPE_CHOICES)
    per_meal = models.IntegerField()
   
    
class Dashboard(models.Model):
    ACTIVE_CHOICES = (
        ('green', 'Green'),
        ('yellow', 'Yellow'),
        ('red', 'Red')
    )


    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15, unique=True)
    service_id = models.CharField(max_length=10, unique=True)
    current_plan = models.ForeignKey(
        Package, on_delete=models.CASCADE, null=True, blank=True)
    balance = models.IntegerField(default=0)
    image = models.ImageField(
        upload_to='uploads/profile', null=True, blank=True)

    flexibility = models.IntegerField(default=0)
    flexibility_used = models.IntegerField(default=0)
    reduce_balance = models.BooleanField(
        default=True, help_text="Uncheck to stop balance reduction of this user")

    def save(self, *args, **kwargs):
        # Check if the instance is being created (not yet saved)
        # if not self.pk:
        #     if len(self.phone) > 10:
        #         last_10_digit = self.phone[-10:]
        #     else:
        #         last_10_digit = self.phone
        #     self.service_id = last_10_digit

        # if not self.meal_status:
        #     meal_off = MealOff.objects.create()
        #     self.meal_status = meal_off
        # elif self.meal_status and self.meal_status.status == True:
        #     self.reduce_balance = False
        # elif self.meal_status == 'None' and self.meal_status.status == False:
        #     self.reduce_balance = True
        super().save(*args, **kwargs)

    @property
    def active(self):
        if self.balance > 160:
            return 'green'
        elif 0 < self.balance <= 160:
            return 'yellow'
        else:
            return 'red'

    def toggle_flexibility(self):
        if not self.reduce_balance:
            # Check if there is remaining flexibility
            if self.flexibility > 0:
                self.flexibility -= 1
                self.flexibility_used += 1  # Increase flexibility_used by 1

        self.save()

    def __str__(self):
        return self.phone


class Payment(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('expired', 'Expired'),
    )

    dashboard = models.ForeignKey(
        Dashboard, related_name='payments', on_delete=models.PROTECT)
    payment_method = models.CharField(max_length=10)
    sender_number = models.CharField(max_length=15)
    transaction_id = models.CharField(max_length=30)
    plan = models.CharField(max_length=100)
    type = models.CharField(max_length=20, blank=True, null=True)
    total_amount = models.IntegerField(default=0)
    started_date = models.DateTimeField(auto_now_add=True)
    expire_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='active', null=True, blank=True)
    confirmed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # if not self.id:  # type: ignore
        #     # If this is a new instance, set started_date to the current time
        #     self.started_date = timezone.now()
        #     # self.expire_date = self.started_date + timezone.timedelta(days=self.plan)
        #     if self.plan in '3 Days':
        #         self.expire_date = self.started_date + \
        #             timezone.timedelta(days=3)
        #     elif self.plan in '7 Days':
        #         self.expire_date = self.started_date + \
        #             timezone.timedelta(days=7)
        #     elif self.plan in '15 Days':
        #         self.expire_date = self.started_date + \
        #             timezone.timedelta(days=15)
        #     elif self.plan in '30 Days':
        #         self.expire_date = self.started_date + \
        #             timezone.timedelta(days=30)

        # if not self.id:  # type: ignore # If it's a new instance
        #     # Check if the user already has an active plan
        #     active_plan_exists = Payment.objects.filter(user=self.user,
        #                                                 expire_date__gt=timezone.now()).exists()
        #     if active_plan_exists and not self.user.is_staff:
        #         raise ValueError(
        #             'You already have an active plan. Please wait until it expires.')
        if self.confirmed:
            try:
                print("inside try",self.dashboard)
                dashbord = Dashboard.objects.filter(phone=self.dashboard)
                # dashbord.
                print("dashbord is :",dashbord)
            except:
                 print("An exception occurred")

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Payment - User:, Method: {self.payment_method}, Transaction ID: {self.transaction_id}"
  
    
    
    
    
    
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    number_in_stock = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.name}--{self.number_in_stock}"
    
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    number_of_items = models.PositiveBigIntegerField()
    
    def __str__(self):
        return f"{self.number_of_items}--{self.product.name}"
    


   # For prooxy model
   
class TaskStatus(models.IntegerChoices):
    TODO = 1
    IN_PROGRESS = 2
    COMPLETED = 3
    
class Task(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=TaskStatus.choices)
    
    
    def __str__(self):
        return self.name
    
    
    
# lets create custom manager
class InProgressTask(Task):
    class Meta:
        proxy = True
        ordering = ('created_at',) # added custom ordering
    class Manager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status=TaskStatus.IN_PROGRESS)
        
    # we want to do something if the task is added for first time
    def save(self, *args, **kwargs):
        if self._state.adding:
            self.status = TaskStatus.IN_PROGRESS
        super().save(*args, **kwargs)
        
    objects = Manager()
    
    