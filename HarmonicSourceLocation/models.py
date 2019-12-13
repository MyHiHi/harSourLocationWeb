from django.db import models

# Create your models here.

class Site(models.Model):
    id=models.IntegerField( '主键',primary_key=True);
    name=models.CharField(max_length=64,null=True)
    description=models.CharField(max_length=64,null=True)
    rank=models.IntegerField(null=True)
    connectionTypeID=models.IntegerField(null=True)
    # DecimalField处理起来麻烦
    # nominalBaseV= models.DecimalField( max_digits=19, decimal_places=10,null=True)
    nominalBaseV= models.FloatField( null=True)
    levelV=models.FloatField(null=True)
    unitcode=models.CharField(max_length=50,null=True)
    stationID=models.IntegerField(null=True)
    ShortCircuitCapacity=models.FloatField( null=True)
    tableID=models.IntegerField(null=True)
class  BaseData(models.Model):
    id=models.IntegerField( '主键',primary_key=True) 
    V=models.FloatField("电压",null=True)
    I=models.FloatField("电流", null=True)
    Site_id = models.ForeignKey(Site,on_delete=models.CASCADE,db_column="site_id",related_name='Site_id')
    
