# Generated by Django 2.1.5 on 2019-02-12 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0002_fotobanner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fotobanner',
            old_name='title',
            new_name='nome',
        ),
    ]
