# Generated by Django 3.1.2 on 2020-10-14 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0007_auto_20201013_0921'),
    ]

    operations = [
        migrations.AddField(
            model_name='production',
            name='amount',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='production',
            name='harvest_area',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='crop',
            name='crop_type',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='crop',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='district',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
