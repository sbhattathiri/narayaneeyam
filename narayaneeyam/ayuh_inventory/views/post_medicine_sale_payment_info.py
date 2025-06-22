from ayuh_inventory import (
    forms,
    models,
)
from django.views.generic.edit import (
    CreateView,
)
from django.urls import (
    reverse_lazy,
)


class MedicineSalePaymentInfoCreateView(CreateView):
    model = models.MedicineSalePaymentInfo
    form_class = forms.MedicineSalePaymentInfoForm
    template_name = "ayuh_inventory/post_payment_info_template.html"
    pk_url_kwarg = "pk"
    context_object_name = "sale"

    def get_success_url(self):
        return reverse_lazy("get_medicine_sale", kwargs={"pk": self.object.id})

    def get_initial(self):
        # Prepopulate the 'sale' field using the sale id from URL
        sale = models.MedicineSale.objects.get(pk=self.kwargs["pk"])
        return {"sale": sale}

    def form_valid(self, form):
        # Ensure that the sale field is set properly, even if disabled in form
        form.instance.sale = models.MedicineSale.objects.get(pk=self.kwargs["pk"])
        return super().form_valid(form)

    # def get_success_url(self):
    #     return reverse_lazy("get_medicine_sale", kwargs={"pk": self.object.sale.id})
    #
    # def get_initial(self):
    #     # Prepopulate the 'sale' field using the sale id from URL
    #     sale = models.MedicineSale.objects.get(pk=self.kwargs["pk"])
    #     return {"sale": sale}
    #
    # def get_form(self, form_class=None):
    #     form = super().get_form(form_class)
    #     # Make the 'sale' field readonly/disabled
    #     form.fields["sale"].disabled = True
    #     return form
    #
    # def form_valid(self, form):
    #     # Ensure that the sale field is set properly, even if disabled in form
    #     form.instance.sale = models.MedicineSale.objects.get(pk=self.kwargs["pk"])
    #     return super().form_valid(form)
