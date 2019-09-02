from django.db import models



class Person(models.Model):
    first_name = models.CharField(max_length=200, default='Null')
    last_name = models.CharField(max_length=200, default='Null')
    phone=models.CharField(max_length=14,default='Null')
    email_address=models.CharField(max_length=200,default='Null')

    def __str__(self):
        return self.first_name

class Buildings(models.Model):
    tenant=models.CharField(max_length=200, default='Null')
    building_name=models.CharField(max_length=200, default='Null')
    contact_number=models.CharField(max_length=200, default='Null')

    def __str__(self):
        return self.building_name

#in html












#contact2=Person(first_name='John',last_name='Dow',phone='0584890064',email_address='me@my.com')
