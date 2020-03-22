from django.db import models
from django.contrib.auth.models import *
# Create your models here.
from django.db import models
import datetime
from django.contrib.auth.models import *


class Students(models.Model):
    stu_id=models.IntegerField()
    name=models.CharField(max_length=128)
    gender=models.CharField(max_length=32)
    college=models.CharField(max_length=128)
    city=models.CharField(max_length=128)
    facebook_url=models.CharField(max_length=256)
    profile_picture=models.CharField(max_length=512)
    dept_id=models.IntegerField()
    sub1_id=models.IntegerField()
    sub2_id=models.IntegerField()
    sub3_id=models.IntegerField()
    sub1 = models.IntegerField()
    sub2 = models.IntegerField()
    sub3 = models.IntegerField()
    last_synced = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.name


