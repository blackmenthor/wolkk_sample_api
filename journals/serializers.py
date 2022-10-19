from rest_framework import serializers

from journals.models import Journal


class JournalSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(required=False, write_only=True)

    class Meta:
        model = Journal
        fields = '__all__'
