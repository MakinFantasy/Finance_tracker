# Generated by Django 4.2.11 on 2024-04-29 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]