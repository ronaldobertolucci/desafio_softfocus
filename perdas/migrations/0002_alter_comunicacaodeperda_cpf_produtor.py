# Generated by Django 4.1 on 2022-08-26 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perdas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comunicacaodeperda',
            name='cpf_produtor',
            field=models.CharField(max_length=11, null=True),
        ),
    ]
