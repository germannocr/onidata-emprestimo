# Generated by Django 3.1 on 2020-09-07 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimo_api', '0003_auto_20200831_2033'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('valor_nominal', models.CharField(max_length=20)),
                ('taxa_juros', models.DecimalField(decimal_places=2, max_digits=4)),
                ('endereco_ip', models.CharField(max_length=12)),
                ('data_solicitacao', models.CharField(max_length=10)),
                ('banco', models.CharField(max_length=60)),
                ('nome_cliente', models.CharField(max_length=120)),
                ('saldo_devedor', models.CharField(max_length=20)),
                ('created_by_user', models.IntegerField()),
            ],
            options={
                'db_table': 'emprestimo',
            },
        ),
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('data_pagamento', models.CharField(max_length=10)),
                ('valor_pagamento', models.CharField(max_length=20)),
                ('created_by_user', models.IntegerField()),
                ('identificador_emprestimo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emprestimo_api.emprestimo')),
            ],
            options={
                'db_table': 'pagamento',
            },
        ),
        migrations.DeleteModel(
            name='Naver',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
