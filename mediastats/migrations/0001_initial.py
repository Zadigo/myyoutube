# Generated by Django 3.1.1 on 2020-12-20 12:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stories', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('videos', '0004_auto_20201220_1336'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(default='fcdf1b0155', max_length=100)),
                ('duration', models.FloatField(default=0.0)),
                ('ended_at', models.FloatField(default=0.0)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('story', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stories.story')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('video', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='videos.video')),
            ],
        ),
    ]