# API/teneastapi/teneastapp/models.py
from django.db import models
from django.contrib.auth.models import User

class Inquiry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    questions = models.JSONField(default=list)  # Store questions as JSON with default empty list
    answers = models.JSONField(default=list)    # Store answers as JSON with default empty list

    def __str__(self):
        return f"Inquiry by {self.user.username}"