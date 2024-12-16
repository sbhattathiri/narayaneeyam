from rest_framework import serializers
from ayuh_patient import models


class PatientProfile(serializers.ModelSerializer):

    class Meta:
        model = models.PatientProfile
        fields = "__all__"
