# Generated by Django 3.2.3 on 2022-02-25 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prospects',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
