# Generated by Django 2.1.7 on 2020-02-11 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_registeredmembers_remarks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registeredmembers',
            name='remarks',
        ),
    ]
