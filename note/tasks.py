from celery import shared_task
from .models import Note
import random
import string

@shared_task
def generate_random_titles():
    notes = Note.objects.all()
    for note in notes:
        random_title = ''.join(random.choices(string.ascii_letters, k=10))
        note.title = random_title
        note.save()
        print(f"Changed title for note ID {note.id} to: {random_title}")
