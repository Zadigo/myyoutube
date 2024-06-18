# Generated by Django 5.0.4 on 2024-06-18 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0006_alter_report_category_alter_report_reference'),
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
            field=models.CharField(default='cd34d43e8dc7eaf7f3ed', max_length=100, unique=True),
        ),
    ]
