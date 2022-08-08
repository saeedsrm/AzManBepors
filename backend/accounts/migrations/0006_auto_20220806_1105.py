# Generated by Django 3.2 on 2022-08-06 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_customuser_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='آیا مدیر است؟'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
    ]