# Generated by Django 5.1.2 on 2024-10-20 17:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('confronto', '0002_alter_confronto_dta_confronto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confronto',
            name='dta_confronto',
            field=models.DateField(default=datetime.datetime(2024, 10, 20, 14, 56, 14, 185397)),
        ),
    ]