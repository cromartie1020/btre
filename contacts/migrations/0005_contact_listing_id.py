# Generated by Django 4.0.2 on 2022-03-13 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_remove_contact_listing_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='listing_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
