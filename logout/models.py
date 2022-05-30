from django.db import models

class Contract_new(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    service = models.IntegerField(db_column='Service')
    client = models.IntegerField(db_column='Client')
    master = models.IntegerField(db_column='Master')
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Contract_new'