# Generated by Django 3.1.6 on 2021-02-13 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parsing', '0002_auto_20210213_0848'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='created_date',
            new_name='created',
        ),
    ]
