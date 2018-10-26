# Generated by Django 2.1.2 on 2018-10-19 22:26

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("noauth", "0004_auto_20181019_0006")]

    operations = [
        migrations.AddField(
            model_name="authcode",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="authcode",
            name="modified_date",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="user",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="user",
            name="modified_date",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
