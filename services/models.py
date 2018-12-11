from django.db import models
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from django.utils.text import slugify

from core.models import TimeStampedModel


class Category(TimeStampedModel):
    '''A category'''
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True, default='')
    desc = models.TextField()
    slug = models.SlugField(null=False, blank=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        '''Return string representation of a category.'''
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)


class Service(TimeStampedModel):
    '''A service'''
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Category, on_delete=models.CASCADE) # change this to category later
    title = models.CharField(max_length=50, blank=True, default='')
    desc = models.TextField()
    slug = models.SlugField(null=False, blank=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        '''Return string representation of a service'''
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Service, self).save(*args, **kwargs)


class Package(TimeStampedModel):
    '''A service'''
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True, default='')
    desc = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    url = models.URLField(max_length=128, db_index=True,unique=True,blank=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        '''Return string representation of a service'''
        return self.title
