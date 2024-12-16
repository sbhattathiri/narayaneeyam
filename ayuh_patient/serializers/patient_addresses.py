from rest_framework import serializers
from ayuh_patient import models


class PatientAddress(serializers.ModelSerializer):

    class Meta:
        model = models.PatientAddress
        fields = "__all__"
