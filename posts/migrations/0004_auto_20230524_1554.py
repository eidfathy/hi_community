# Generated by Django 3.2 on 2023-05-24 12:54

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_placesprofile'),
        ('posts', '0003_likepostuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='postuser',
            name='dislikes',
            field=models.ManyToManyField(blank=True, related_name='dislikes', to='accounts.UserProfile'),
        ),
        migrations.AlterField(
            model_name='likepostuser',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('usre', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='post_images')),
                ('caption', models.TextField()),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('no_of_like', models.IntegerField(default=0)),
                ('creater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='createdpost', to='accounts.userprofile')),
            ],
        ),
    ]
