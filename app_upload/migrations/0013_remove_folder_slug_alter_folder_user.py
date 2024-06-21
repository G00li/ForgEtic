# Generated by Django 5.0.6 on 2024-06-20 19:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_upload", "0012_alter_folder_slug"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="folder",
            name="slug",
        ),
        migrations.AlterField(
            model_name="folder",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="folders",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
