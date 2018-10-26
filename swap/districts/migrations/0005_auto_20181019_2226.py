# Generated by Django 2.1.2 on 2018-10-19 22:26

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("districts", "0004_district_slug")]

    operations = [
        migrations.RemoveField(model_name="building", name="deleted"),
        migrations.RemoveField(model_name="district", name="deleted"),
        migrations.AddField(
            model_name="building",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="building",
            name="deleted_at",
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AddField(
            model_name="building",
            name="modified_date",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="district",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="district",
            name="deleted_at",
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AddField(
            model_name="district",
            name="modified_date",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
