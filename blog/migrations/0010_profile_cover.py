# Generated by Django 3.2.3 on 2021-05-20 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_profile_writer'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cover',
            field=models.ImageField(default='', upload_to='coverpic'),
        ),
    ]