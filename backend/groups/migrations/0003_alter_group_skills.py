# Generated by Django 3.2 on 2021-04-21 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_auto_20210421_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='skills',
            field=models.CharField(default='C, Data Modelling, User Interfaces', max_length=1000),
        ),
    ]