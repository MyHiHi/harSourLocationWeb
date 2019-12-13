# Generated by Django 2.1.15 on 2019-12-13 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseData',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='主键')),
                ('V', models.FloatField(null=True, verbose_name='电压')),
                ('I', models.FloatField(null=True, verbose_name='电流')),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='主键')),
                ('name', models.CharField(max_length=64, null=True)),
                ('description', models.CharField(max_length=64, null=True)),
                ('rank', models.IntegerField(null=True)),
                ('connectionTypeID', models.IntegerField(null=True)),
                ('nominalBaseV', models.FloatField(null=True)),
                ('levelV', models.FloatField(null=True)),
                ('unitcode', models.CharField(max_length=50, null=True)),
                ('stationID', models.IntegerField(null=True)),
                ('ShortCircuitCapacity', models.FloatField(null=True)),
                ('tableID', models.IntegerField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='basedata',
            name='Site_id',
            field=models.ForeignKey(db_column='site_id', on_delete=django.db.models.deletion.CASCADE, related_name='Site_id', to='HarmonicSourceLocation.Site'),
        ),
    ]