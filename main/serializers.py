from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from main.models import EditRequest


class EditRequestSerializer(ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = EditRequest
        fields = ['doc', 'deadline', 'owner', 'category', 'description']
