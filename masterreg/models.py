from django.db import models

# Create your models here.
class Masters(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    person = models.ForeignKey('Persons', models.DO_NOTHING, db_column='Person_ID', blank=True, null=True)  # Field name made lowercase.
    experience = models.IntegerField(db_column='Experience', blank=True, null=True)  # Field name made lowercase.
    salary = models.DecimalField(db_column='Salary', max_digits=7, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Masters'


class Persons(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_name', max_length=20)  # Field name made lowercase.
    first_name = models.CharField(db_column='First_name', max_length=20)  # Field name made lowercase.
    father_name = models.CharField(db_column='Father_name', max_length=20, blank=True, null=True)  # Field name made lowercase.
    phone_number = models.CharField(db_column='Phone_number', unique=True, max_length=13)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Persons'