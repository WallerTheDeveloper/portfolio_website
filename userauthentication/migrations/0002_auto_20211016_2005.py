# Generated by Django 3.2.8 on 2021-10-16 18:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('userauthentication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AddField(
            model_name='user',
            name='user_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
