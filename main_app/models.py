from django.db import models
import uuid

class Book(models.Model):
    name = models.CharField(max_length=100)
    unique_id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False)


