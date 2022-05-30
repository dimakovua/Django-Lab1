from django.db import models

class Persons(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_name', max_length=20)  # Field name made lowercase.
    first_name = models.CharField(db_column='First_name', max_length=20)  # Field name made lowercase.
    father_name = models.CharField(db_column='Father_name', max_length=20, blank=True, null=True)  # Field name made lowercase.
    phone_number = models.CharField(db_column='Phone_number', unique=True, max_length=13)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Persons'

class Services(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    services_name = models.CharField(db_column='Services_name', unique=True, max_length=10)  # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=10)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=7, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Services'

class Masters(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    person = models.ForeignKey('Persons', models.DO_NOTHING, db_column='Person_ID', blank=True, null=True)  # Field name made lowercase.
    experience = models.IntegerField(db_column='Experience', blank=True, null=True)  # Field name made lowercase.
    salary = models.DecimalField(db_column='Salary', max_digits=7, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Masters'

class Specialization(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    master = models.ForeignKey(Masters, models.DO_NOTHING, db_column='Master_ID', blank=True, null=True)  # Field name made lowercase.
    service = models.ForeignKey(Services, models.DO_NOTHING, db_column='Service_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Specialization'
