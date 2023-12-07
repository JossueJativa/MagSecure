from django.db import models
from userLogin.models import Users

# Create your models here.
class Workload(models.Model):
    name = models.CharField(max_length=50, null=False)

class TypeAssets(models.Model):
    name = models.CharField(max_length=50, null=False)

class SubtypeAssets(models.Model):
    name = models.CharField(max_length=50, null=False)
    type = models.ForeignKey(TypeAssets, null=True)

class Departments(models.Model):
    name = models.CharField(max_length=50, null=False)
    description = models.TextField(max_length=200, null=False)
    workload = models.ManyToOneRel(Workload)

class Assets(models.Model):
    code = models.CharField(max_length=5)
    origin = models.CharField(max_length=20)
    name = models.TextField(max_length=20)
    tipe = models.ForeignKey(TypeAssets)
    responsableArea = models.ForeignKey(Departments, null=False)
    responsableUser = models.ForeignKey(Users, null=False)
    ubicationTipe = models.CharField(max_length=20)
    ubication = models.CharField(max_length=20)
    quantity = models.IntegerField()
    Characteristic = models.TextField(max_length=50)
    