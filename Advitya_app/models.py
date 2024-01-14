from django.db import models
from django.contrib.auth.models import User
from django.db import models
# from django.contrib.auth import get_user_model
from django.contrib.auth import get_user_model
# class Event(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     date = models.DateField()

#     def __str__(self):
#         return self.name
    
class Socio_trivia_reg(models.Model):
    schoolname = models.CharField(max_length=200, default="")
    address = models.CharField(max_length=200, default="")
    # event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, blank=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE,  null=True, blank=True)  # Add a foreign key to the User model

    def __str__(self):
        return f"{self.schoolname} "
    # models.py



class Activity(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    activity_type = models.CharField(max_length=50, choices=[("Activity 1", "Activity 1"), ("Activity 2", "Activity 2")], null=True)

    def __str__(self):
        return f"{self.name} - {self.activity_type}"


class UserActivityRegistration(models.Model):
    # auth_user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=1)
    email = models.CharField(max_length=50, default="no")

    name_user = models.CharField(max_length=50, default="no")
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.name_user} - {self.activity.name}"
    
class UserActivityRegistrationInitial(models.Model):
    # auth_user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=1)
    email = models.CharField(max_length=50, default="no")

    name_user = models.CharField(max_length=50, default="no")
    # activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)

from django.db import models
from django.contrib.auth.models import User
from django.db import models
# from django.contrib.auth import get_user_model
from django.contrib.auth import get_user_model
# class Event(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     date = models.DateField()

#     def __str__(self):
#         return self.name
    
class Socio_trivia_reg(models.Model):
    schoolname = models.CharField(max_length=200, default="")
    address = models.CharField(max_length=200, default="")
    # event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, blank=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE,  null=True, blank=True)  # Add a foreign key to the User model

    def __str__(self):
        return f"{self.schoolname} "
    # models.py



# class Activity(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField(blank=True, null=True)
#     activity_type = models.CharField(max_length=50, choices=[("Activity 1", "Activity 1"), ("Activity 2", "Activity 2")], null=True)

#     def __str__(self):
#         return f"{self.name} - {self.activity_type}"
    
 

from django.db import models

# Create your models here.

class UserAccount(models.Model):
    name = models.CharField(max_length=200, default="")
    email = models.CharField( max_length=254 , default="")
    phone = models.CharField(max_length=12 , default="")
    college = models.CharField( max_length=200, default = "")

    City = models.CharField( max_length=50, default = "")
    events = models.TextField(default="")
    
    # profession = models.CharField( max_length=50, default = "")
    # referral = models.CharField( max_length=50, default = "")

   

    def __str__(self):
        return self.name
    
    # models.py

from django.db import models
from django.contrib.auth.models import User

class ActivityRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name_user = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)  # Assuming you have an Activity model defined

    # Add other fields as needed

    def __str__(self):
        return f"{self.name_user} - {self.activity}"