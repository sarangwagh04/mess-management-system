# billing/models.py

from django.db import models
from django.contrib.auth.models import User

class HostelMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional fields for hostel member information

class Attendance(models.Model):
    member = models.ForeignKey(HostelMember, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
