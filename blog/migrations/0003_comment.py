# Generated by Django 3.2.3 on 2021-05-14 09:05

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210514_1141'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_by', models.CharField(max_length=100)),
                ('comment_text', models.TextField(max_length=300)),
                ('comment_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('comment_on_blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blog')),
            ],
        ),
    ]
