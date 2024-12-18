from rest_framework import viewsets
from backend.ayuh_patient import models, serializers


class PatientProfileAPI(viewsets.ModelViewSet):
    queryset = models.PatientProfile.objects.all()
    serializer_class = serializers.PatientProfile
