# Generated by Django 5.0.7 on 2024-08-25 12:58

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='image/post')),
                ('body', models.TextField()),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('draft', 'draft'), ('published', 'Published')], default='draft', max_length=10)),
            ],
            options={
                'ordering': ('-publish',),
            },
        ),
    ]
