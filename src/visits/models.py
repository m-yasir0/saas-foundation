from sqlite3 import Timestamp
from django.db import models

class PageVisit(models.Model):
    path = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
