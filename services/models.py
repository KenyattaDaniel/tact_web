from django.db import models
from django.contrib.auth.models import User
from core.models import TimeStampedModel


class Service(TimeStampedModel):
    '''A service type'''
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True, default='')
    desc = models.TextField()

    class Meta:
        ordering = ('created',)
    
    def __str__(self):
        '''Return string representation of a service.'''
        return self.title 


class Offering(TimeStampedModel):
    '''A subset of a service type'''
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True, default='')
    desc = models.TextField()

    class Meta:
        ordering = ('created',)

    def __str__(self):
        '''Return string representation of an offering.'''
        return self.title