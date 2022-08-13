# Generated by Django 3.1.1 on 2020-12-20 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0005_auto_20201220_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='visibility',
            field=models.CharField(choices=[('Public', 'Public'), ('Private', 'Private')], default='Public', max_length=50),
        ),
        migrations.AlterField(
            model_name='video',
            name='category',
            field=models.CharField(choices=[('Film and animation', 'Film And Animation'), ('Music', 'Music'), ('Gaming', 'Gaming'), ('Entertainment', 'Entertainment'), ('Fashion', 'Fashion'), ('Beauty', 'Beauty')], default='Entertainment', max_length=50),
        ),
        migrations.AlterField(
            model_name='video',
            name='comment_strategy',
            field=models.CharField(choices=[('Allow all comments', 'Allow All Comments'), ('Hold all comments for review', 'Hold For Review'), ('Disable all comments', 'Disable All')], default='Allow all comments', max_length=150),
        ),
        migrations.AlterField(
            model_name='video',
            name='recording_language',
            field=models.CharField(choices=[('French', 'French'), ('English', 'English')], default='English', max_length=50),
        ),
        migrations.AlterField(
            model_name='video',
            name='reference',
            field=models.CharField(default='5fc47a43ea', max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='visibility',
            field=models.CharField(choices=[('Public', 'Public'), ('Private', 'Private')], default='Public', max_length=50),
        ),
    ]
