from django.db import models
from django.utils import timezone




class Person(models.Model):
    firstname_text = models.CharField(max_length=200)
    lastname_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.firstname_text,lastname_text



class Choice(models.Model):
    question = models.ForeignKey(Person, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

#p2=Person.objects.create(firstname_text='John', lastname_text='Doe',pub_date=timezone.now)
#p1=Person.objects.create(firstname_text='Neil', lastname_text='Hofman',pub_date=timezone.now)
