# Generated by Django 3.2.12 on 2023-11-18 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_buddy', '0004_friend_tb'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend_tb',
            name='user_id',
            field=models.CharField(default=0, max_length=20),
        ),
    ]
