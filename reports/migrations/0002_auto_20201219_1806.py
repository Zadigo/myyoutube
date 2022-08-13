# Generated by Django 3.1.1 on 2020-12-19 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='category',
            field=models.CharField(choices=[('SEXISM', 'Sexism'), ('Racism', 'Racism')], default='SEXISM', max_length=50),
        ),
        migrations.AlterField(
            model_name='report',
            name='reference',
            field=models.CharField(default='e4156cde1390e492622b', max_length=100, unique=True),
        ),
    ]