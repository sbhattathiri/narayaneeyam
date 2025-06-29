# Generated by Django 4.2.17 on 2025-02-01 13:26

import django.db.models.deletion
from django.db import (
    migrations,
    models,
)


class Migration(migrations.Migration):

    dependencies = [
        ("ayuh_consultation", "0003_alter_prescription_consultation"),
    ]

    operations = [
        migrations.AlterField(
            model_name="consultationattachment",
            name="consultation",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="consultation_attachment",
                to="ayuh_consultation.consultation",
            ),
        ),
    ]
