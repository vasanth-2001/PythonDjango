# Generated by Django 4.2.17 on 2025-01-07 03:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogger',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='blogger',
            name='email',
        ),
        migrations.RemoveField(
            model_name='blogger',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='blogger',
            name='last_name',
        ),
    ]
