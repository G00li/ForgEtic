# Generated by Django 5.0.6 on 2024-06-18 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_upload", "0003_uploadfile_rename_file_folder"),
    ]

    operations = [
        migrations.AlterField(
            model_name="folder",
            name="id",
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="folder",
            name="name",
            field=models.CharField(max_length=50),
        ),
    ]