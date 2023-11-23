from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Note
from .serializers import NoteSerializer


class OrderPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 100


class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    pagination_class = OrderPagination
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer) -> None:
        serializer.save(user=self.request.user)
