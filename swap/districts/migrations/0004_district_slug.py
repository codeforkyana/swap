# Generated by Django 2.1.2 on 2018-10-04 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("districts", "0003_building_slug")]

    operations = [
        migrations.AddField(
            model_name="district",
            name="slug",
            field=models.SlugField(default="No"),
            preserve_default=False,
        )
    ]
