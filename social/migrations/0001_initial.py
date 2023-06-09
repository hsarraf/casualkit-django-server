# Generated by Django 4.1.7 on 2023-02-28 11:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('player', '0001_initial'),
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Social',
            fields=[
                ('userId', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('socialId', models.CharField(max_length=20, unique=True)),
                ('createDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('log', models.TextField(blank=True, default='')),
                ('friends', models.ManyToManyField(blank=True, related_name='player_friends', to='player.player')),
                ('pendingFriends', models.ManyToManyField(blank=True, related_name='player_pendingFriends', to='player.player')),
                ('teams', models.ManyToManyField(blank=True, to='team.team')),
            ],
        ),
    ]
