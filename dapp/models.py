from django.db import models

# Create your models here.


class Dapp(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    email = models.EmailField(blank=False, default='')
    phonenumber = models.IntegerField(blank=False, default='')
    description = models.CharField(max_length=20, blank=False, default='')
    
    class Meta:
        ordering = ('id',)

