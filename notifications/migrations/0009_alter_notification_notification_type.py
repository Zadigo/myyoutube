# Generated by Django 5.0.6 on 2024-07-15 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0008_alter_notification_notification_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notification_type',
            field=models.CharField(choices=[('Message', 'Message'), ('Follow', 'Follow'), ('Like', 'Like'), ('Donation', 'Donation'), ('Shoutout', 'Shoutout')], default='Follow', max_length=50),
        ),
    ]
