# Generated by Django 2.2 on 2019-04-28 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_user_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_app',
            field=models.BooleanField(default=False),
        ),
    ]
