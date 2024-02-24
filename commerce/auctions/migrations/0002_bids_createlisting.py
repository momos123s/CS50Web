# Generated by Django 3.2.19 on 2024-01-12 07:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateListing',
            fields=[
                ('listingID', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('startDate', models.DateTimeField()),
                ('creatorID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bids',
            fields=[
                ('biddID', models.BigAutoField(primary_key=True, serialize=False)),
                ('dateOfBirth', models.DateTimeField(auto_now_add=True)),
                ('bidderID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('listID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.createlisting')),
            ],
        ),
    ]