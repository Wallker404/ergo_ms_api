from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Tag(models.Model):
    name = models.CharField(max_length=100, default='')

class Category(models.Model):
    name = models.CharField(max_length=100, default='')
    parentcategory = models.ForeignKey('self', on_delete=models.PROTECT)

class Object_Type(models.Model):
    name = models.CharField(max_length=100, default='')

class Object(models.Model):
    objectlink = models.CharField(max_length=255, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.ForeignKey(Object_Type, on_delete=models.CASCADE)

class ShortCode(models.Model):
    name = models.CharField(max_length=100, default='')
    content = models.TextField(default='')
    ispage = models.BooleanField(default=False)
    date_of_creation = models.DateField(default=timezone.now)
    last_update = models.DateTimeField(default=timezone.now)
    user =models.ForeignKey(User, on_delete=models.CASCADE)

class ShortCode_Parameter(models.Model):
    key = models.CharField(max_length=100, default='')
    value = models.TextField(default='')
    shortcode = models.ForeignKey(ShortCode, on_delete=models.CASCADE)