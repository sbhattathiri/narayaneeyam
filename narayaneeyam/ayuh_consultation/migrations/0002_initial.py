# Generated by Django 4.2.17 on 2024-12-29 09:10

import django.db.models.deletion
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
        ("ayuh_consultation", "0001_initial"),
        ("ayuh_staff", "0001_initial"),
        ("ayuh_patient", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="consultation",
            name="doctor",
            field=models.ForeignKey(
                blank=True,
                db_column="doctor",
                limit_choices_to={"designation": "Doctor"},
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="consulting_doctor",
                to="ayuh_staff.staff",
            ),
        ),
        migrations.AddField(
            model_name="consultation",
            name="patient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="consulting_patient",
                to="ayuh_patient.patient",
            ),
        ),
        migrations.AddField(
            model_name="consultation",
            name="updated_by",
            field=models.ForeignKey(
                blank=True,
                help_text="The user who last updated this record.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="%(class)s_updated_by",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
