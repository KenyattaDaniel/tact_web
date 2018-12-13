from django.db import models
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from django.utils.text import slugify

from core.models import TimeStampedModel


class Category(TimeStampedModel):
    '''A service category'''
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True, default='')
    subtitle = models.CharField(max_length=50, blank=True, default='')
    desc = models.TextField()

    class Meta:
        ordering = ('created',)

    def __str__(self):
        '''Return string representation of a category.'''
        return self.title


class Service(TimeStampedModel):
    '''A service'''
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True, default='')
    subtitle = models.CharField(max_length=50, blank=True, default='')
    desc = models.TextField()

    class Meta:
        ordering = ('created',)

    def __str__(self):
        '''Return string representation of a service'''
        return self.title


class Package(TimeStampedModel):
    '''A service package'''
    HOURLY = 'HR'
    WEEKLY = 'WK'
    MONTHLY = 'MO'
    QUARTERLY = 'QT'
    YEARLY = 'YR'
    BESPOKE = 'BS'

    BILL_FREQUENCY_CHOICES = (
    ('HOURLY', 'Hourly'),
    ('WEEK', 'Weekly'),
    ('MONTHLY', 'Monthly'),
    ('QUARTERLY', 'Quarterly'),
    ('YEARLY', 'Yearly'),
    ('BESPOKE', 'Bespoke'),
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True, default='')
    desc = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    bill_frequency = models.CharField(max_length=10, choices=BILL_FREQUENCY_CHOICES, default=MONTHLY)
    url = models.URLField(max_length=128, db_index=True,unique=True,blank=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        '''Return string representation of a service'''
        return self.title
