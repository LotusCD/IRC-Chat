# Generated by Django 3.2 on 2021-04-10 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('irc', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='timestap',
            new_name='timestamp',
        ),
    ]