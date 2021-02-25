from rest_framework import serializers
from .models import *


class CompanyAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyAccount
        fields = "__all__"