# Generated by Django 4.1 on 2022-08-30 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perdas', '0003_comunicacaodeperda_analista'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comunicacaodeperda',
            options={'ordering': ['-data_colheita'], 'verbose_name': 'Comunicação de perda', 'verbose_name_plural': 'Comunicações de perda'},
        ),
    ]
