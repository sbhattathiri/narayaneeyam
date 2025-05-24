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


class MultipleMedicineSaleCreateView(CreateView):

    model = models.MedicineSale
    form_class = forms.MedicineSaleForm
    template_name = "ayuh_inventory/post_multiple_medicine_sale_template.html"
    success_url = reverse_lazy("list_medicine")  # or whatever your URL name is

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context["formset"] = forms.MedicineSaleItemsFormSet(self.request.POST)
        else:
            context["formset"] = forms.MedicineSaleItemsFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context["formset"]

        if formset.is_valid():
            self.object = form.save()
            items = formset.save(commit=False)
            for item in items:
                item.sale = self.object
                item.patient = self.object.patient
                item.save()
            formset.save_m2m()
            return redirect(self.success_url)

        return self.form_invalid(form)
