# Generated by Django 3.2.12 on 2023-11-27 04:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_buddy', '0015_auto_20231127_0355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment_tb',
            name='commenter_id',
        ),
        migrations.AlterField(
            model_name='comment_tb',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_buddy.register_tb'),
        ),
    ]
