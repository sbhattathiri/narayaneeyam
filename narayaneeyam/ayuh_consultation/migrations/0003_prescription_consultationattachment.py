# Generated by Django 4.2.17 on 2024-12-29 14:31

import uuid

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
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("ayuh_consultation", "0002_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Prescription",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "prescription_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("medicine", models.CharField(max_length=255)),
                ("instructions", models.TextField(blank=True, null=True)),
                (
                    "consultation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="consulting_patient",
                        to="ayuh_consultation.consultation",
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
                "abstract": False,
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "bulk_change",
                    "bulk_delete",
                    "bulk_add",
                    "export",
                ),
            },
        ),
        migrations.CreateModel(
            name="ConsultationAttachment",
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
                    "attachment",
                    models.ImageField(upload_to="consultation_attachments/"),
                ),
                (
                    "consultation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="attachments",
                        to="ayuh_consultation.consultation",
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
                "abstract": False,
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "bulk_change",
                    "bulk_delete",
                    "bulk_add",
                    "export",
                ),
            },
        ),
    ]