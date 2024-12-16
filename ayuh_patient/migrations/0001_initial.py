# Generated by Django 4.2.17 on 2024-12-16 10:23

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django_pg_jsonschema.fields
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('created_by', models.EmailField(blank=True, max_length=254, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('patient_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=15, null=True)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('emergency_contact_person_name', models.CharField(blank=True, max_length=255, null=True)),
                ('emergency_contact_person_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PatientAddress',
            fields=[
                ('created_by', models.EmailField(blank=True, max_length=254, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='ayuh_patient.patient')),
                ('billing_address', django_pg_jsonschema.fields.JSONSchemaField(blank=True, check_schema_in_db=False, null=True, schema={'$schema': 'http://json-schema.org/draft-07/schema#', 'properties': {'PIN': {'type': 'integer'}, 'address_line_1': {'type': 'string'}, 'address_line_2': {'type': 'string'}, 'address_line_3': {'type': 'string'}, 'address_line_4': {'type': 'string'}}, 'required': ['PIN'], 'type': 'object'})),
                ('billing_address_is_shipping_address', models.BooleanField(default=False)),
                ('shipping_address', django_pg_jsonschema.fields.JSONSchemaField(blank=True, check_schema_in_db=False, null=True, schema={'$schema': 'http://json-schema.org/draft-07/schema#', 'properties': {'PIN': {'type': 'integer'}, 'address_line_1': {'type': 'string'}, 'address_line_2': {'type': 'string'}, 'address_line_3': {'type': 'string'}, 'address_line_4': {'type': 'string'}}, 'required': ['PIN'], 'type': 'object'})),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PatientProfile',
            fields=[
                ('patient_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ayuh_patient.patient')),
                ('primary_care_provider', models.CharField(blank=True, db_comment='Name of the Clinic/Hospital which the ayuh_patient goes to', max_length=255, null=True)),
                ('primary_physician_name', models.CharField(blank=True, max_length=255, null=True)),
                ('primary_physician_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('primary_physician_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('blood_type', models.IntegerField(blank=True, choices=[('O +ve', 'O_POS'), ('O -ve', 'O_NEG'), ('A +ve', 'A_POS'), ('A -ve', 'A_NEG'), ('B +ve', 'B_POS'), ('B -ve', 'B_NEG'), ('AB +ve', 'AB_POS'), ('AB -ve', 'AB_NEG')], null=True)),
                ('known_allergies', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), blank=True, null=True, size=None)),
                ('known_medication_allergies', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), blank=True, null=True, size=None)),
                ('previous_surgeries', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), blank=True, null=True, size=None)),
                ('pre_existing_medications', models.TextField(blank=True, null=True)),
                ('pre_existing_health_conditions', models.TextField(blank=True, null=True)),
                ('smoking_status', models.BooleanField(blank=True, null=True)),
                ('drinking_status', models.BooleanField(blank=True, null=True)),
                ('substance_abuse_status', models.BooleanField(blank=True, null=True)),
                ('dietary_preference', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('ayuh_patient.patient',),
        ),
    ]
