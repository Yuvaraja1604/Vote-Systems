# Generated by Django 3.0 on 2023-07-29 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reg',
            fields=[
                ('name', models.CharField(max_length=20)),
                ('dob', models.CharField(max_length=15)),
                ('em', models.CharField(max_length=15)),
                ('sa', models.CharField(max_length=15)),
                ('ad', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]