# Generated by Django 4.0.2 on 2022-03-13 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_contact_listing_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='listing_id',
        ),
    ]
