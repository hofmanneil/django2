from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    #1 to 1 relationship with User
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)                             #we have control on Accounts
