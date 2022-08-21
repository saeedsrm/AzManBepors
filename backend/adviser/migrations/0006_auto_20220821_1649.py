# Generated by Django 3.2 on 2022-08-21 12:19

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('adviser', '0005_auto_20220812_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='date_time',
            field=django_jalali.db.models.jDateField(auto_now=True, verbose_name='تاریخ پاسخ به سوال'),
        ),
        migrations.AlterField(
            model_name='createnewquestion',
            name='data_create',
            field=django_jalali.db.models.jDateField(auto_now=True, verbose_name='تاریخ ایجاد سوال'),
        ),
    ]
