# Generated by Django 5.0.6 on 2024-06-23 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_upload", "0017_folder_parent_folder"),
    ]

    operations = [
        migrations.AlterField(
            model_name="folder",
            name="name",
            field=models.CharField(max_length=50),
        ),
    ]