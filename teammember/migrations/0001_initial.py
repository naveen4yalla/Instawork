# Generated by Django 4.0.1 on 2022-01-12 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('choice', models.CharField(choices=[('memeber', "Regular - Can't delete members"), ('admin', 'Admin - Can delete members')], default='user', max_length=20)),
            ],
            options={
                'ordering': ['create'],
            },
        ),
    ]
