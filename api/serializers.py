from dataclasses import field
import imp
from rest_framework import serializers
from rest_api.models import Etudiant


class EtudiantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etudiant
        fields = '__all__'
