# Generated by Django 2.2 on 2019-04-30 14:36

from django.db import migrations, models
import django.db.models.deletion
import luzeiros.radio.models.helpers.music


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0002_auto_20190428_1546'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigIntegerField(editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=30)),
                ('artwork', models.ImageField(blank=True, upload_to=luzeiros.radio.models.helpers.music.path_for_album)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'radio_albums',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigIntegerField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=30)),
                ('photo', models.ImageField(blank=True, upload_to=luzeiros.radio.models.helpers.music.path_for_artist)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'radio_artists',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigIntegerField(editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=30)),
                ('duration', models.IntegerField(blank=True)),
                ('preview_file', models.FileField(upload_to=luzeiros.radio.models.helpers.music.path_for_track)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='radio.Album')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='radio.Artist')),
            ],
            options={
                'db_table': 'radio_tracks',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='radio.Artist'),
        ),
    ]
