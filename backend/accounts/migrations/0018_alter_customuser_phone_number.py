# Generated by Django 3.2 on 2022-08-26 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_auto_20220826_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True, verbose_name='تلفن همراه'),
        ),
    ]