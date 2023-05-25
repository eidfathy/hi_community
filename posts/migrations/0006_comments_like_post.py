# Generated by Django 3.2 on 2023-05-24 14:04

import datetime
from django.db import migrations, models
import django.db.models.deletion
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_placesprofile'),
        ('posts', '0005_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('image', models.ImageField(upload_to=posts.models.image_post_user)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('tags', models.CharField(blank=True, max_length=100)),
                ('creater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='createdpost', to='accounts.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='posts.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='accounts.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('creater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='createdcomment', to='accounts.userprofile')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='posts.post')),
            ],
        ),
    ]