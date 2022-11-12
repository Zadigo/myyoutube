# Generated by Django 4.1.3 on 2022-11-12 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0003_alter_notification_notification_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notification_type',
            field=models.CharField(choices=[('Message', 'Message'), ('Follow', 'Follow'), ('Like', 'Like'), ('Donation', 'Donation'), ('Shoutout', 'Shoutout')], default='Follow', max_length=50),
        ),
    ]
