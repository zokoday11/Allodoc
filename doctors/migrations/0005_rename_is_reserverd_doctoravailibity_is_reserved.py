# Generated by Django 3.2.3 on 2021-06-20 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0004_doctoravailibity_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctoravailibity',
            old_name='is_reserverd',
            new_name='is_reserved',
        ),
    ]
