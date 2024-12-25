from ayuh_patient import (
    models,
    serializers,
)
from rest_framework import (
    viewsets,
)


class PatientProfileAPI(viewsets.ModelViewSet):
    queryset = models.PatientProfile.objects.all()
    serializer_class = serializers.PatientProfile
