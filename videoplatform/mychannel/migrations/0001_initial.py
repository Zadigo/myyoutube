# Generated by Django 5.0.6 on 2024-10-18 20:17

import django.db.models.deletion
import mychannel.utils
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChannelTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserChannel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=2000)),
                ('banner', models.ImageField(blank=True, null=True, upload_to=mychannel.utils.banners_directory_path)),
                ('category', models.CharField(choices=[('Beauty', 'Beauty'), ('Commentary', 'Commentary'), ('Corporate', 'Corporate'), ('Other', 'Other')], default='Beauty', max_length=100)),
                ('email', models.CharField(blank=True, max_length=150, null=True)),
                ('instagram', models.CharField(blank=True, max_length=150, null=True)),
                ('tiktok', models.CharField(blank=True, max_length=150, null=True)),
                ('facebook', models.CharField(blank=True, max_length=150, null=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('subscribers', models.ManyToManyField(blank=True, related_name='channel_subscribers', to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(blank=True, to='mychannel.channeltag')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='ChannelPlaylist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('user_channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mychannel.userchannel')),
            ],
        ),
        migrations.CreateModel(
            name='BlockedChannel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('channel', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='mychannel.userchannel')),
            ],
        ),
        migrations.AddIndex(
            model_name='userchannel',
            index=models.Index(condition=models.Q(('is_verified', True)), fields=['is_verified'], name='verified_channel'),
        ),
        migrations.AddIndex(
            model_name='channelplaylist',
            index=models.Index(fields=['name'], name='mychannel_c_name_be0c40_idx'),
        ),
    ]
