from django.conf import settings
from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=510, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["-created_at"]

