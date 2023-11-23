from django.urls import path, include
from rest_framework import routers

from .views import NoteViewSet

router = routers.DefaultRouter()
router.register("note", NoteViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "note"
