# Generated by Django 4.0.3 on 2022-04-10 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_rename_dmaks_dmaksmin_d1_rename_dmin_dmaksmin_d2'),
    ]

    operations = [
        migrations.AddField(
            model_name='tabel',
            name='rata',
            field=models.CharField(max_length=5, null=True),
        ),
    ]