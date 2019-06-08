# Generated by Django 2.2.1 on 2019-06-08 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Absence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('shift_zone', models.CharField(max_length=15)),
                ('comment', models.TextField(default='なし', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Alternative',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('shift_zone', models.CharField(max_length=15)),
                ('comment', models.TextField(default='なし', max_length=200)),
            ],
        ),
    ]
