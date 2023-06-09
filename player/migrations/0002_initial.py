# Generated by Django 4.1.7 on 2023-02-28 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('social', '0001_initial'),
        ('userProfile', '0001_initial'),
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='social',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='social.social'),
        ),
        migrations.AddField(
            model_name='player',
            name='userProfile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userProfile.userprofile'),
        ),
    ]
