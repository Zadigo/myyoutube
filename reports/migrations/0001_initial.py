# Generated by Django 3.1.1 on 2020-12-19 14:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comments', '0001_initial'),
        ('videos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(default='2f8cdfee647b6a31dc41', max_length=100, unique=True)),
                ('category', models.CharField(choices=[('SEXISM', 'Sexism'), ('Racism', 'Racism')], default='SEXISM', max_length=50)),
                ('notes', models.TextField(blank=True, max_length=500, null=True)),
                ('is_correct', models.BooleanField(default=False)),
                ('reviewed', models.BooleanField(default=False)),
                ('reviewed_on', models.DateTimeField(auto_now_add=True)),
                ('comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='comments.comment')),
                ('reply', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='comments.reply')),
                ('reviewed_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('video', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='videos.video')),
            ],
        ),
    ]