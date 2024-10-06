# Generated by Django 5.0.6 on 2024-07-15 16:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlists', '0001_initial'),
        ('videos', '0009_alter_video_category_alter_video_comment_strategy_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='is_intelligent',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='visibility',
            field=models.CharField(choices=[('Public', 'Public'), ('Private', 'Private')], default='Public', max_length=50),
        ),
        migrations.AddIndex(
            model_name='playlist',
            index=models.Index(condition=models.Q(('is_intelligent', True)), fields=['is_intelligent'], name='intelligent_playlists'),
        ),
    ]
