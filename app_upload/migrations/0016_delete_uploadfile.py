# Generated by Django 5.0.6 on 2024-06-23 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app_upload", "0015_alter_uploadfile_file_alter_uploadfile_title"),
    ]

    operations = [
        migrations.DeleteModel(
            name="UploadFile",
        ),
    ]
