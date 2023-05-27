# Generated by Django 3.2 on 2023-05-26 22:07

import datetime
from django.db import migrations, models
import django.db.models.deletion
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20230527_0052'),
        ('posts', '0004_alter_post_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostPlaces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to=posts.models.image_post_user)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('tags', models.CharField(blank=True, max_length=100)),
                ('creater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='createdpost', to='accounts.placesprofile')),
            ],
        ),
    ]
