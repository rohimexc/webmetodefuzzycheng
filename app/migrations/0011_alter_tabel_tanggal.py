# Generated by Django 4.0.2 on 2022-04-11 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_tabel_tanggal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tabel',
            name='tanggal',
            field=models.DateField(null=True),
        ),
    ]
