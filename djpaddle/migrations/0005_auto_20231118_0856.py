# Generated by Django 3.1.7 on 2023-11-17 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djpaddle', '0004_auto_20210119_0436'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='paused_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='subscription',
            name='paused_from',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='subscription',
            name='paused_reason',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
