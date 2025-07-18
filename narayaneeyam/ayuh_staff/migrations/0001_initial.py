# Generated by Django 4.2.17 on 2025-01-20 06:59

import django.db.models.deletion
import phonenumber_field.modelfields
from django.conf import (
    settings,
)
from django.db import (
    migrations,
    models,
)


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Staff",
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
                (
                    "title",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Mr.", "MR"),
                            ("Ms.", "MS"),
                            ("Mrs.", "MRS"),
                            ("Prof.", "PROF"),
                            ("Dr.", "DR"),
                        ],
                        default="",
                        null=True,
                    ),
                ),
                (
                    "first_name",
                    models.CharField(blank=True, default="", max_length=255, null=True),
                ),
                (
                    "middle_name",
                    models.CharField(blank=True, default="", max_length=255, null=True),
                ),
                (
                    "last_name",
                    models.CharField(blank=True, default="", max_length=255, null=True),
                ),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("MALE", "Male"),
                            ("FEMALE", "Female"),
                            ("OTHER", "Other"),
                        ],
                        default="",
                        null=True,
                    ),
                ),
                ("date_of_birth", models.DateField(blank=True, null=True)),
                (
                    "designation",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Doctor", "DOCTOR"),
                            ("Therapist", "THERAPIST"),
                            ("Cleaner", "CLEANER"),
                            ("Cook", "COOK"),
                        ],
                        default="",
                        null=True,
                    ),
                ),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                (
                    "phone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True, max_length=128, null=True, region="IN"
                    ),
                ),
                ("date_of_joining", models.DateField(blank=True, null=True)),
                ("date_of_leaving", models.DateField(blank=True, null=True)),
                ("active", models.BooleanField(default=True)),
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
                "unique_together": {
                    ("first_name", "middle_name", "last_name", "email")
                },
            },
        ),
    ]
