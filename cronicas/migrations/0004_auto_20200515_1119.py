# Generated by Django 3.0.5 on 2020-05-14 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cronicas', '0003_auto_20200515_1109'),
    ]

    operations = [
        migrations.RenameField(
            model_name='documento',
            old_name='autor',
            new_name='autores',
        ),
    ]
