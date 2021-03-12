# Generated by Django 3.0.12 on 2021-03-09 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmpId', models.CharField(max_length=8)),
                ('name', models.CharField(max_length=32)),
            ],
            options={
                'ordering': ('-EmpId',),
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StuId', models.CharField(max_length=8)),
                ('name', models.CharField(max_length=32)),
            ],
            options={
                'ordering': ('-StuId',),
            },
        ),
    ]
