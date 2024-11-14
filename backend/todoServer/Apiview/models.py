from django.db import models

class Todo(models.Model):
    
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(blank=True, default='')
    completed = models.BooleanField(default=False)
