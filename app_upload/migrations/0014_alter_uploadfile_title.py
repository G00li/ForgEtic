# Generated by Django 5.0.6 on 2024-06-21 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_upload", "0013_remove_folder_slug_alter_folder_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="uploadfile",
            name="title",
            field=models.CharField(max_length=255),
        ),
    ]
