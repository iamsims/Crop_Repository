# Generated by Django 3.1.2 on 2020-11-09 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0009_auto_20201109_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='production',
            name='crop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cropss', to='production.crop'),
        ),
        migrations.AlterField(
            model_name='production',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='districtss', to='production.district'),
        ),
    ]
