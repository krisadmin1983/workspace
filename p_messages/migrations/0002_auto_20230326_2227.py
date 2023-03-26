# Generated by Django 3.2.7 on 2023-03-26 14:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('p_messages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communitymessage',
            name='message',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='communitymessage',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
