# Generated by Django 4.2.11 on 2024-04-29 16:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_remove_expense_tags_delete_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='date_created',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 4, 29, 16, 25, 26, 523461, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='expense',
            name='date_created',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 4, 29, 16, 25, 26, 523800, tzinfo=datetime.timezone.utc)),
        ),
    ]
