# Generated by Django 5.1.2 on 2024-11-17 12:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('confronto', '0005_alter_confronto_dta_confronto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confronto',
            name='dta_confronto',
            field=models.DateField(default=datetime.datetime(2024, 11, 17, 9, 5, 34, 588060)),
        ),
    ]
