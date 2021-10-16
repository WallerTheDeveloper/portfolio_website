from django.db import models
import uuid

class User(models.Model):
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=40)
    user_id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False)

    def __str__(self):
        return f'{self.email}'
