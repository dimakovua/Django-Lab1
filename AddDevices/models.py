# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Clients(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    person = models.ForeignKey('Persons', models.DO_NOTHING, db_column='Person_ID', blank=True, null=True)  # Field name made lowercase.
    accumulative_card = models.CharField(db_column='Accumulative_card', unique=True, max_length=10, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Clients'

class Persons(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_name', max_length=20)  # Field name made lowercase.
    first_name = models.CharField(db_column='First_name', max_length=20)  # Field name made lowercase.
    father_name = models.CharField(db_column='Father_name', max_length=20, blank=True, null=True)  # Field name made lowercase.
    phone_number = models.CharField(db_column='Phone_number', unique=True, max_length=13)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Persons'
        
class Devices(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=10)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=10, blank=True, null=True)  # Field name made lowercase.
    breakage = models.CharField(db_column='Breakage', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Devices'

class OwnershipDocument(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    owner = models.ForeignKey(Clients, models.DO_NOTHING, db_column='Owner_ID', blank=True, null=True)  # Field name made lowercase.
    device = models.ForeignKey(Devices, models.DO_NOTHING, db_column='Device_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Ownership_document'


