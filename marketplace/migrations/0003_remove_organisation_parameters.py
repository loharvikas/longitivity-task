# Generated by Django 3.2.7 on 2021-09-12 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0002_organisation_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organisation',
            name='parameters',
        ),
    ]