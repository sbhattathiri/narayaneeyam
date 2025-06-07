from django.views.generic import (
    ListView,
)

from ayuh_admission import (
    models,
)


class AdmissionListView(ListView):
    model = models.Admission
    template_name = "ayuh_admission/list_admission_template.html"
    context_object_name = "admissions"

    def get_queryset(self):
        admissions = models.Admission.objects.all()

        admissions_data = []
        for admission in admissions:
            admissions_data.append(
                {
                    "patient": admission.patient_hash_id,
                    "doctor": admission.consultation.doctor__full_name,
                    "consultation": admission.consultation,
                    "admission_date": admission.admission_date,
                    "room": admission.room,
                    "discharge_date": admission.discharge_date,
                }
            )

        return admissions_data
