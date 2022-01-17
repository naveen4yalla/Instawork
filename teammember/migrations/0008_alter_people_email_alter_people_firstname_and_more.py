# Generated by Django 4.0.1 on 2022-01-17 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teammember', '0007_alter_people_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='firstname',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='people',
            name='lastname',
            field=models.CharField(max_length=40, null=True),
        ),
    ]