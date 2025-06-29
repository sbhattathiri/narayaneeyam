# Generated by Django 4.2.17 on 2025-06-17 05:42

import django.db.models.deletion
from django.conf import (
    settings,
)
from django.db import (
    migrations,
    models,
)


class Migration(migrations.Migration):

    dependencies = [
        (
            "ayuh_admission",
            "0002_alter_admission_options_admission_created_at_and_more",
        ),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("ayuh_facility", "0002_alter_room_room_location"),
    ]

    operations = [
        migrations.CreateModel(
            name="RoomOccupancy",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField(blank=True, null=True)),
                (
                    "admission",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="room_occupancy_admission",
                        to="ayuh_admission.admission",
                    ),
                ),
                (
                    "room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="room_occupancy_room",
                        to="ayuh_facility.room",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        blank=True,
                        help_text="The user who last updated this record.",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_updated_by",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-end_date"],
            },
        ),
    ]
