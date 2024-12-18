from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.



class Seeker(models.Model):

    # CITY_CHOICES = (
    # (None, 'choose your city'),
    # ('city1', "city1"),
    # ('city2', "city2"),
    # ('city3', "city3"),
    # )

    seeker_name = models.CharField(max_length=100, unique=False) 
    seeker_email = models.EmailField(max_length=24)
    seeker_password = models.CharField(max_length=100)   

    seeker_mobile = models.CharField(max_length=15)
    # seeker_dob = models.DateField(max_length=100, blank=True, null=True, default=None)
    seeker_gender = models.CharField(max_length=20)
    seeker_occupation =  models.CharField(max_length=50) 

    seeker_religion = models.CharField(max_length=24, default='')  
    seeker_caste = models.CharField(max_length=24, default='')  
    seeker_language = models.CharField(max_length=50)   
    
    # seeker_city = models.CharField(choices=CITY_CHOICES, max_length=15)
    seeker_city = models.CharField(max_length=15, default='')  
    seeker_state =  models.CharField(max_length=50)
    seeker_country =  models.CharField(max_length=50)
    

    def __str__(self):
        return self.seeker_name
    
    class Meta:
        db_table="Seeker"


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
 
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        
    post_save.connect(create_user_profile, sender=User)

    def __str__(self):
        if not self.user:
            return "Anonymous"
        return self.user.username

    # Override the save method of the model
    def save(self, **kwargs):
        super().save()
   
    