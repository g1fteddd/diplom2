# Generated by Django 3.2.18 on 2023-03-16 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='keywords1',
        ),
    ]