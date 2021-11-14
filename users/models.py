from __future__ import unicode_literals
from django.db import models

# Create your models here.
from django.contrib import admin

from django.db.models.fields.related import ForeignKey

class account(models.Model):
    username = models.CharField(null=False,help_text="Enter your phone number",max_length=15)
    password = models.CharField(max_length=30)
    id =models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of Product.
        """
        return reverse('account-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.id


class customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(default=0,primary_key=True,max_length=15)
    dateofbirth = models.DateField(null=False)
    Address = models.CharField(max_length=50)
    id_account = models.ForeignKey(account,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Credit_card(models.Model):
    id_card = models.PositiveBigIntegerField(default=0, primary_key=True)
    id_user = models.ForeignKey(account,on_delete=models.CASCADE)
    bank = models.CharField(max_length=15)
    expired_day = models.DateTimeField()
    account_name = models.CharField(max_length=100)

    def __str__(self):
        return self.id_card
