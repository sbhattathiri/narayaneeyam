from ayuh_patient import (
    models,
)
from rest_framework import (
    serializers,
)


class PatientProfile(serializers.ModelSerializer):

    class Meta:
        model = models.PatientProfile
        fields = "__all__"
