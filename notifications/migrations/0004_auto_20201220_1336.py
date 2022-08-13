# Generated by Django 3.1.1 on 2020-12-20 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0003_auto_20201219_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notification_type',
            field=models.CharField(choices=[('Message', 'Message'), ('Follow', 'Follow'), ('Like', 'Like'), ('Donation', 'Donation'), ('Shoutout', 'Shoutout')], default='Follow', max_length=50),
        ),
    ]
