# Generated by Django 4.1.2 on 2022-10-19 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_sample', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=50),
        ),
    ]