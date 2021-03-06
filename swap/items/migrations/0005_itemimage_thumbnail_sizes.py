# Generated by Django 2.1.2 on 2018-10-07 21:24

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("items", "0004_auto_20181007_1542")]

    operations = [
        migrations.AddField(
            model_name="itemimage",
            name="thumbnail_sizes",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.SmallIntegerField(), default=[], size=None
            ),
            preserve_default=False,
        )
    ]
