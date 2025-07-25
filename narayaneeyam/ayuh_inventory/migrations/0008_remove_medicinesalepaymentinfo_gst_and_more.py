# Generated by Django 4.2.17 on 2025-06-22 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ayuh_inventory', '0007_medicinesalepaymentinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicinesalepaymentinfo',
            name='gst',
        ),
        migrations.RemoveField(
            model_name='medicinesalepaymentinfo',
            name='gst_amount',
        ),
        migrations.RemoveField(
            model_name='medicinesalepaymentinfo',
            name='total_amount',
        ),
        migrations.RemoveField(
            model_name='medicinesalepaymentinfo',
            name='total_amount_with_gst',
        ),
        migrations.AddField(
            model_name='medicine',
            name='gst',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=10),
        ),
        migrations.AddField(
            model_name='medicinesalepaymentinfo',
            name='consultation_fee',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='medicinesalepaymentinfo',
            name='gross_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='medicinesalepaymentinfo',
            name='gst_on_consultation_fee',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='medicinesalepaymentinfo',
            name='total_consultation_amount_with_gst',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='medicinesalepaymentinfo',
            name='total_gst_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='medicinesalepaymentinfo',
            name='total_sale_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='medicinesalepaymentinfo',
            name='total_sale_amount_with_gst',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
    ]
