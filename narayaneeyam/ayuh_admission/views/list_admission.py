from ayuh_admission import (
    models,
)
from django.views.generic import (
    ListView,
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
                    "id": admission.id,
                    "patient": admission.consultation.patient,
                    "doctor": admission.consultation.doctor,
                    "consultation": admission.consultation,
                    "admission_date": admission.admission_date,
                    "room": admission.room,
                    "discharge_date": admission.discharge_date,
                }
            )

        return admissions_data
