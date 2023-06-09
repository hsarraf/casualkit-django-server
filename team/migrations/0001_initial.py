# Generated by Django 4.1.7 on 2023-02-28 11:15

from django.db import migrations, models
import django.utils.timezone
import team.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamId', models.CharField(default=team.models.generate_team_id, max_length=20, unique=True)),
                ('createDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('log', models.TextField(blank=True, default='')),
                ('people', models.ManyToManyField(to='player.player')),
            ],
        ),
    ]
