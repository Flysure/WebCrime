# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CrimeTable(models.Model):
    field1 = models.TextField(blank=True, null=True)  # This field type is a guess.
    crnumber = models.TextField(db_column='CRnumber', blank=True, primary_key=True)  # Field name made lowercase. This field type is a guess.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    victim = models.TextField(db_column='Victim', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    datereported = models.TextField(db_column='DateReported', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    location = models.TextField(db_column='Location', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    lat = models.TextField(db_column='Lat', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    lng = models.TextField(db_column='Lng', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'crime_table'
