# Generated by Django 3.2 on 2022-08-09 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adviser', '0003_answer_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='sub_category',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='زیر دسته بندی'),
        ),
    ]
