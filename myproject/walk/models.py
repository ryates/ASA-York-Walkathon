from django.db import models
from django.forms import ModelForm

class Team(models.Model):
    TeamTypes = (
        ('Corporate', 'Corporate'),
        ('Group', 'Group'),
        ('Honorarium', 'Honorarium'),
    )
    type = models.CharField(max_length=10, choices=TeamTypes)
    captain = models.ForeignKey('Person', related_name='captain', blank=True, null=True)
    name = models.CharField(max_length=50)
    company = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Person(models.Model):
    PersonTypes = (
        ('Walker', 'Walker'),
        ('Captain', 'Captain'),
    )
    ShirtSizes = (
        ('Youth-M', 'Youth-M'),
        ('Youth-L', 'Youth-L'),
        ('Adult-Small', 'Adult-Small'),
        ('Adult-Medium', 'Adult-Medium'),
        ('Adult-Large', 'Adult-Large'),
        ('Adult-XL', 'Adult-XL'),
        ('Adult-2X', 'Adult-2X'),
    )
    type = models.CharField(max_length=10, choices=PersonTypes)
    size = models.CharField(max_length=15, choices=ShirtSizes)
    team = models.ForeignKey(Team, blank=True, null=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    emergency_first = models.CharField(max_length=30)
    emergency_last = models.CharField(max_length=30)
    emergency_phone = models.CharField(max_length=10)
    
    def __unicode__(self):
        return self.last_name+' '+self.first_name


class Sponsor(models.Model):
    walker = models.ForeignKey(Person)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    paid = models.BooleanField(default=False)

    def __unicode__(self):
        return self.last_name+' '+self.first_name

class WalkerForm(ModelForm):
    class Meta:
        model = Person

class NewTeamForm(ModelForm):
    class Meta:
        model = Team

