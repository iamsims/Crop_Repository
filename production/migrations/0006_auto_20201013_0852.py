# Generated by Django 3.1.2 on 2020-10-13 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0005_auto_20201013_0850'),
    ]

    operations = [
        migrations.RenameField(
            model_name='district',
            old_name='region',
            new_name='area',
        ),
    ]
