# Generated by Django 4.2.17 on 2025-01-07 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_blogger_contact_remove_blogger_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogger',
            name='contact',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='blogger',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='blogger',
            name='first_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='blogger',
            name='last_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
