# Generated by Django 4.2.17 on 2024-12-26 16:23

import phonenumber_field.modelfields

from django.db import (
    migrations,
    models,
)


class Migration(migrations.Migration):

    dependencies = [
        ("ayuh_patient", "0002_alter_patientprofile_blood_type_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="patient",
            name="emergency_contact_person_name",
        ),
        migrations.RemoveField(
            model_name="patient",
            name="emergency_contact_person_phone",
        ),
        migrations.RemoveField(
            model_name="patientprofile",
            name="blood_type",
        ),
        migrations.RemoveField(
            model_name="patientprofile",
            name="date_of_birth",
        ),
        migrations.AddField(
            model_name="patient",
            name="blood_type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("O +ve", "O_POS"),
                    ("O -ve", "O_NEG"),
                    ("A +ve", "A_POS"),
                    ("A -ve", "A_NEG"),
                    ("B +ve", "B_POS"),
                    ("B -ve", "B_NEG"),
                    ("AB +ve", "AB_POS"),
                    ("AB -ve", "AB_NEG"),
                ],
                default="",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="patient",
            name="date_of_birth",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="patient",
            name="gender",
            field=models.CharField(
                blank=True,
                choices=[("Male", "MALE"), ("Female", "FEMALE"), ("Other", "OTHER")],
                default="",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="patientprofile",
            name="emergency_contact_person_phone",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True, max_length=128, null=True, region="IN"
            ),
        ),
        migrations.AddField(
            model_name="patientprofile",
            name="general_lifestyle",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Heavy Labor", "HEAVY_LABOR"),
                    ("Active", "ACTIVE"),
                    ("Sedentary", "SEDENTARY"),
                    ("Other", "OTHER"),
                ],
                default="",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="patient",
            name="title",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Mr", "Mr"),
                    ("Ms", "Ms"),
                    ("Mrs", "Mrs"),
                    ("Prof.", "Prof"),
                    ("Dr.", "Dr"),
                ],
                default="",
                null=True,
            ),
        ),
    ]
