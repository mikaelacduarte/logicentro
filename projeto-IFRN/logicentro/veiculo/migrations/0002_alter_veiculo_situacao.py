# Generated by Django 5.1.1 on 2024-10-07 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veiculo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veiculo',
            name='situacao',
            field=models.CharField(choices=[('A', 'Ativo'), ('I', 'Inativo')], max_length=1),
        ),
    ]
