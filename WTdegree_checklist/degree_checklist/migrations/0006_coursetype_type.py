# Generated by Django 3.1 on 2023-09-24 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('degree_checklist', '0005_auto_20230923_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursetype',
            name='type',
            field=models.CharField(choices=[('Core', 'Core'), ('Major', 'Major')], default=0, max_length=20),
        ),
    ]