# Generated by Django 3.2.19 on 2024-01-15 16:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20240112_1343'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bids',
            old_name='dateOfBirth',
            new_name='dateOfBid',
        ),
        migrations.RemoveField(
            model_name='createlisting',
            name='startDate',
        ),
        migrations.AddField(
            model_name='createlisting',
            name='startdate',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
