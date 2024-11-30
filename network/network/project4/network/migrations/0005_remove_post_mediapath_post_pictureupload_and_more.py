# Generated by Django 5.0.4 on 2024-10-12 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0004_alter_post_postid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='mediaPath',
        ),
        migrations.AddField(
            model_name='post',
            name='pictureUpload',
            field=models.ImageField(null=True, upload_to='pictures/'),
        ),
        migrations.AddField(
            model_name='post',
            name='videoUpload',
            field=models.FileField(null=True, upload_to='videos/'),
        ),
    ]