# Generated by Django 4.1.3 on 2022-11-28 16:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("project", "0003_alter_issue_reporter"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="creator",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="projects",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
