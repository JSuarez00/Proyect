# Generated by Django 4.2.3 on 2023-07-24 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miportafolio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proyecto',
            old_name='tranding',
            new_name='trading',
        ),
    ]
