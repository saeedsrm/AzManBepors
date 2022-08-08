# Generated by Django 3.2 on 2022-08-06 08:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20220806_1105'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='responder',
            options={'verbose_name': 'کاربر راهنما', 'verbose_name_plural': 'کاربران راهنما'},
        ),
        migrations.AlterField(
            model_name='responder',
            name='descriptions',
            field=models.TextField(verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='responder',
            name='fields_of_activity',
            field=models.TextField(verbose_name='زمینه های فعالیت'),
        ),
        migrations.AlterField(
            model_name='responder',
            name='interests',
            field=models.TextField(verbose_name='علاقه مندی ها'),
        ),
        migrations.AlterField(
            model_name='responder',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
    ]