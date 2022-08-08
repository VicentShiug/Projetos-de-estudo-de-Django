# Generated by Django 4.0.6 on 2022-07-29 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0002_alter_categoria_dt_criacao_transacao'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transacao',
            options={'verbose_name_plural': 'Transações'},
        ),
        migrations.AlterField(
            model_name='transacao',
            name='data',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='transacao',
            name='observacoes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
