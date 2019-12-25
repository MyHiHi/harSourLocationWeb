# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Site(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    # Field name made lowercase.
    connectiontypeid = models.SmallIntegerField(
        db_column='connectionTypeID', blank=True, null=True)
    # Field name made lowercase.
    nominalbasev = models.FloatField(
        db_column='nominalBaseV', blank=True, null=True)
    # Field name made lowercase.
    levelV = models.FloatField(db_column="levelV", blank=True, null=True)
    unitcode = models.CharField(max_length=50, blank=True, null=True)
    # Field name made lowercase.
    stationid = models.IntegerField(
        db_column='stationID', blank=True, null=True)
    # Field name made lowercase.
    shortcircuitcapacity = models.FloatField(
        db_column='ShortCircuitCapacity', blank=True, null=True)
    # Field name made lowercase.
    tableid = models.BigIntegerField(
        db_column='tableID', blank=True, null=True)

    class Meta:
        db_table = 'Site'
        verbose_name_plural = u"监测点表"


class BaseData(models.Model):
    # Field name made lowercase.
    site = models.ForeignKey(Site,  to_field="id",
                             related_name="Site_id", db_column='Site_id', on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    # Field name made lowercase.
    v = models.FloatField(db_column='V', blank=True, null=True)
    # Field name made lowercase.
    i = models.FloatField(db_column='I', blank=True, null=True)

    class Meta:
        db_table = 'Base_Data'
        unique_together = (('site', 'id'),)

        verbose_name_plural = u"基础数据表"
    primary = ('site', 'id')


# class MyI(models.Model):
#     id = models.IntegerField(primary_key=True)
#     # Field name made lowercase.
#     i = models.CharField(max_length=40, db_column='I', blank=True, null=True)

#     class Meta:
#         db_table = 'MyI'

class Station(models.Model):
    stationid = models.IntegerField(db_column='StationID', primary_key=True)  #Field name made lowercase.
    stationname = models.CharField(db_column='StationName', max_length=200)  # Field name made lowercase.
    manager = models.CharField(db_column='Manager', max_length=200, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=200, blank=True, null=True)  # Field name made lowercase.
    telphone = models.CharField(db_column='TelPhone', max_length=200, blank=True, null=True)  # Field name made lowercase.
    descript = models.CharField(db_column='Descript', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Station'
