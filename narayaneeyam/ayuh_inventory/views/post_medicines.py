from django.urls import (
    reverse_lazy,
)
from django.shortcuts import redirect
from django.views.generic.edit import (
    CreateView,
)

from ayuh_inventory import (
    forms,
    models,
)


class MedicineSaleCreateView(CreateView):
    model = models.MedicineSaleItem
    form_class = forms.MedicineSalesForm
    template_name = "ayuh_inventory/post_medicine_sale_template.html"
    success_url = reverse_lazy("list_medicine")


class MultipleMedicineSaleCreateView(CreateView):
    model = models.MedicineSaleItem
    form_class = forms.MedicineSalesForm
    template_name = "ayuh_inventory/post_multiple_medicine_sale_template.html"
    success_url = reverse_lazy("list_medicine")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context["medicine_sales_item_formset"] = forms.MedicineSaleItemsFormSet(
                self.request.POST
            )
        else:
            context["medicine_sales_item_formset"] = forms.MedicineSalesForm()
        return context

    def form_valid(self, form):
        if self.request.POST:
            form = forms.MedicineSaleItemsFormSet(self.request.POST)
        else:
            form = forms.MedicineSaleItemsFormSet()
        if form.is_valid():
            sale = models.MedicineSale.objects.create()
            sale_items = form.save(commit=False)
            for item in sale_items:
                item.sale = sale
                item.save()
            # return redirect("list_medicine")
            return reverse_lazy("list_medicine")
        else:
            return self.form_invalid(form)
