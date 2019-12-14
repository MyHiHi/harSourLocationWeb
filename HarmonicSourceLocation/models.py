# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BaseData(models.Model):
    site = models.ForeignKey('Site', models.DO_NOTHING, db_column='Site_id', primary_key=True)  # Field name made lowercase.
    id = models.IntegerField()
    v = models.FloatField(db_column='V', blank=True, null=True)  # Field name made lowercase.
    i = models.FloatField(db_column='I', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Base_Data'
        unique_together = (('site', 'id'),)


class Site(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    connectiontypeid = models.SmallIntegerField(db_column='connectionTypeID', blank=True, null=True)  # Field name made lowercase.
    nominalbasev = models.FloatField(db_column='nominalBaseV', blank=True, null=True)  # Field name made lowercase.
    levelV = models.FloatField( db_column="levelV",blank=True, null=True)  # Field name made lowercase.
    unitcode = models.CharField(max_length=50, blank=True, null=True)
    stationid = models.IntegerField(db_column='stationID', blank=True, null=True)  # Field name made lowercase.
    shortcircuitcapacity = models.FloatField(db_column='ShortCircuitCapacity', blank=True, null=True)  # Field name made lowercase.
    tableid = models.BigIntegerField(db_column='tableID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Site'
