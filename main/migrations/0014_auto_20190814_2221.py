# Generated by Django 2.2.4 on 2019-08-14 20:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20190814_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 14, 22, 21, 4, 104461), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_thumbnail',
            field=models.CharField(default='no_image', max_length=200),
        ),
    ]
