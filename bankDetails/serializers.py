from rest_framework import serializers
from .models import Banks, Branches


class BranchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Branches
        fields = ['ifsc', 'branch','address','city','district','state']