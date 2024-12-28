from ayuh_patient import (
    models,
)
from rest_framework import (
    serializers,
)


class PatientAddress(serializers.ModelSerializer):

    class Meta:
        model = models.PatientAddress
        fields = "__all__"
