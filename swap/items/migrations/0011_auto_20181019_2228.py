# Generated by Django 2.1.2 on 2018-10-19 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("items", "0010_auto_20181019_2226")]

    operations = [
        migrations.RenameField(
            model_name="item", old_name="modified_date", new_name="modified_at"
        ),
        migrations.RenameField(
            model_name="itemimage", old_name="modified_date", new_name="modified_at"
        ),
    ]
