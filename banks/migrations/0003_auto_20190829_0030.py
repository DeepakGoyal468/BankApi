# Generated by Django 2.2.4 on 2019-08-28 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0002_auto_20190828_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='address',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='branch',
            name='branch',
            field=models.CharField(max_length=250),
        ),
    ]