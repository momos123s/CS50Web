# Generated by Django 5.0.4 on 2024-11-09 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0017_alter_profile_profileid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='following',
            field=models.ManyToManyField(null=True, related_name='followers', to='network.profile'),
        ),
    ]
