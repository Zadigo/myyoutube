# Generated by Django 5.0.4 on 2024-06-18 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0003_alter_rating_rating_for_alter_rating_rating_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rating_for',
            field=models.CharField(choices=[('Comment', 'Comment'), ('Video', 'Video'), ('Reply', 'Reply')], default='Video', max_length=50),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating_type',
            field=models.CharField(choices=[('Like', 'Like'), ('Dislike', 'Dislike')], default='Like', max_length=50),
        ),
    ]
