# Generated by Django 3.2 on 2023-06-24 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_communitymembership_postcommunity'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='username',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True),
        ),
    ]
