from django.db import (
    models,
)
from django_hashids import (
    HashidsField,
)

from ayuh_core.enums.ayuh_enums import PAYMENT_METHOD_CHOICES
from ayuh_core.models import (
    AyuhModel,
)
from ayuh_patient.models import (
    Patient,
)
from ayuh_inventory.managers import (
    MedicineSaleManager,
    MedicineSaleItemManager,
    MedicineSalePaymentInfoManager,
)


class MedicineSale(AyuhModel):
    # Add optimized manager
    objects = MedicineSaleManager()
    
    sale_id = HashidsField(real_field_name="id")
    sale_date = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(
        Patient,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    customer = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        customer = self.patient or self.customer
        return f"{self.sale_id} to customer {customer} on {self.sale_date:%d-%b-%Y}"

    class Meta:
        verbose_name = "Medicine Sale"
        verbose_name_plural = "Medicine Sales"


class MedicineSaleItem(AyuhModel):
    # Add optimized manager
    objects = MedicineSaleItemManager()
    
    sale = models.ForeignKey(
        "MedicineSale", on_delete=models.CASCADE, related_name="items"
    )
    medicine = models.ForeignKey("Medicine", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.sale} of {self.medicine} : {self.quantity} units"

    class Meta:
        verbose_name = "Medicine Sale Item"
        verbose_name_plural = "Medicine Sale Items"


class MedicineSalePaymentInfo(AyuhModel):
    # Add optimized manager
    objects = MedicineSalePaymentInfoManager()
    
    payment_hash_id = HashidsField(real_field_name="id")
    sale = models.ForeignKey(
        "MedicineSale", on_delete=models.CASCADE, related_name="payment"
    )
    total_sale_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
    )
    total_gst_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
    )
    total_sale_amount_with_gst = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
    )
    consultation_fee = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
    )
    gross_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
    )
    amount_paid = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
    )
    amount_due = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
    )
    payment_method = models.CharField(
        choices=PAYMENT_METHOD_CHOICES,
        null=True,
        blank=True,
        default="",
    )
    payment_due_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.payment_hash_id} worth {self.total_amount_with_gst} by method {self.payment_method}"

    class Meta:
        verbose_name = "Medicine Sale Item"
        verbose_name_plural = "Medicine Sale Items"
