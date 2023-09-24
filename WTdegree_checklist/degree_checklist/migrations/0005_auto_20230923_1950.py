# Generated by Django 3.1 on 2023-09-24 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('degree_checklist', '0004_auto_20230923_1927'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coursetype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Core_category', models.CharField(help_text='010,020, ...', max_length=10)),
                ('Component_area', models.CharField(help_text='Mathematics, Major, ...', max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='type',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='degree_checklist.coursetype'),
        ),
    ]