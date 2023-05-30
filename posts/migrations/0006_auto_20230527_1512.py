# Generated by Django 3.2 on 2023-05-27 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_postplaces'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75, verbose_name='interest')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'interest',
                'verbose_name_plural': 'interests',
            },
        ),
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.AddField(
            model_name='post',
            name='interest',
            field=models.ManyToManyField(related_name='interests', to='posts.Interest'),
        ),
    ]