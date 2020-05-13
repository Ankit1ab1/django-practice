from rest_framework import serializers
from .models import JobModel

class JobSerializers(serializers.ModelSerializer):
    class Meta:
        model=JobModel
        fields='__all__'