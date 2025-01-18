from django.db import models

# Create your models here.


from django.db import models
from django.contrib.auth.models import User

class Suggestion(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    suggestion_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
