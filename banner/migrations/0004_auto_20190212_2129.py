# Generated by Django 2.1.5 on 2019-02-12 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0003_auto_20190212_2120'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fotobanner',
            old_name='bannerprincipal',
            new_name='bannery',
        ),
    ]