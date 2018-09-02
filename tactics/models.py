from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from core.models import TimeStampedModel

# Create your models here.
class Tactic(TimeStampedModel):
    '''A post about a specific tactic'''
    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    image = models.ImageField(upload_to="media")
 
    class Meta:
        ordering = ('-created',)
 
    def __str__(self):
        return self.title