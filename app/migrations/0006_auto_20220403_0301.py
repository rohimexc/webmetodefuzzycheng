# Generated by Django 3.2 on 2022-04-02 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20220403_0256'),
    ]

    operations = [
        migrations.AddField(
            model_name='tabel',
            name='akurasi',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='tabel',
            name='peramalan',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
