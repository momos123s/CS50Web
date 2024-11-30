# Generated by Django 5.0.4 on 2024-11-28 11:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0019_alter_profile_following'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('record', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('UserIDs', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('postID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='network.post')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='amountOfLikes',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='network.likes'),
            preserve_default=False,
        ),
    ]