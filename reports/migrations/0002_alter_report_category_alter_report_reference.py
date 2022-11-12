# Generated by Django 4.1.3 on 2022-11-12 20:48

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
            field=models.CharField(default='9840f7b7ec690b4bdcaf', max_length=100, unique=True),
        ),
    ]