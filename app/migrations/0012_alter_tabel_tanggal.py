# Generated by Django 4.0.2 on 2022-04-11 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_tabel_tanggal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tabel',
            name='tanggal',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
