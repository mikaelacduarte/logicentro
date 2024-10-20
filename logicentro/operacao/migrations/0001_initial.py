# Generated by Django 5.1.2 on 2024-10-20 15:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresa', '0001_initial'),
        ('motorista', '0001_initial'),
        ('veiculo', '0002_alter_veiculo_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operacao',
            fields=[
                ('id_operacao', models.AutoField(primary_key=True, serialize=False)),
                ('placa', models.CharField(max_length=45)),
                ('dta_saida', models.DateTimeField()),
                ('dta_entrada', models.DateTimeField()),
                ('status', models.CharField(default='Pendente', max_length=45)),
                ('nro_mdfe', models.IntegerField(blank=True, null=True)),
                ('nro_notafiscal', models.IntegerField(blank=True, null=True)),
                ('nro_lacre', models.IntegerField(blank=True, null=True)),
                ('empresa_destino', models.ForeignKey(db_column='id_empresa_destino', on_delete=django.db.models.deletion.PROTECT, related_name='empresa_destino', to='empresa.empresa')),
                ('empresa_origem', models.ForeignKey(db_column='id_empresa_origem', on_delete=django.db.models.deletion.PROTECT, related_name='empresa_origem', to='empresa.empresa')),
                ('motorista', models.ForeignKey(db_column='id_motorista', on_delete=django.db.models.deletion.PROTECT, to='motorista.motorista')),
                ('veiculo', models.ForeignKey(db_column='id_veiculo', on_delete=django.db.models.deletion.PROTECT, to='veiculo.veiculo')),
            ],
            options={
                'db_table': 'tb_operacao',
                'indexes': [models.Index(fields=['veiculo'], name='idx_operacao_veiculo'), models.Index(fields=['motorista'], name='idx_operacao_motorista'), models.Index(fields=['empresa_origem'], name='idx_operacao_origem'), models.Index(fields=['empresa_destino'], name='idx_operacao_destino')],
            },
        ),
    ]