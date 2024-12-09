# Generated by Django 5.0.4 on 2024-12-07 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_rename_categoryid_categories_catergorykey_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createlisting',
            name='label',
        ),
        migrations.DeleteModel(
            name='Categories',
        ),
        migrations.AddField(
            model_name='createlisting',
            name='label',
            field=models.CharField(choices=[('FOOD', 'Food and Beverage'), ('ELEC', 'Electronics and Tech'), ('HOME', 'Home and Furniture'), ('FASH', 'Fashion and Accessories'), ('HEALTH', 'Health and Beauty'), ('ENT', 'Entertainment'), ('SPORTS', 'Sports and Outdoors'), ('TOYS', 'Toys and Hobbies'), ('AUTO', 'Automotive'), ('SERV', 'Services'), ('MISC', 'Miscellaneous')], default='MISC', max_length=100),
        ),
    ]
