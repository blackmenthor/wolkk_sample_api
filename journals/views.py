from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from journals.models import Journal
from journals.serializers import JournalSerializer


class JournalViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Journal.objects.all()
    serializer_class = JournalSerializer

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        data = Journal.objects.filter(created_by=user)
        return data.order_by('-created_date')

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
