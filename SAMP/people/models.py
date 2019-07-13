# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30,null=False)
    pswd = models.CharField(max_length=256,null=False)
    cookie_id = models.CharField(max_length=256,null=True)
    cookie_create_time = models.DateTimeField(blank=True,null=True)
    cookie_expire=models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.name

#personal information
class User_info(models.Model):
    name = models.ForeignKey(Person, on_delete=models.CASCADE)
    motto = models.CharField(max_length=100)
    gender = models.IntegerField(choices=((0, "unknow"), (1, "male"), (2, "female")), default=0)
    birth_date = models.DateTimeField(null=True)
    profile = models.ImageField(null=True)

    def __str__(self):
        return self.name

#organization information
class Organizations(models.Model):
    number = models.BigAutoField(primary_key=True)
    organization_name = models.CharField(max_length=30, null=False)
    creater = models.ForeignKey(User_info, related_name='organization1', on_delete=models.CASCADE)
    member = models.ManyToManyField(User_info, related_name='organization2')

    def __str__(self):
        return self.number