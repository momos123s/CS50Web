# Generated by Django 5.0.4 on 2024-11-09 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0015_remove_following_userid_profile_delete_followers_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='User',
            new_name='profileID',
        ),
    ]
