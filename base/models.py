from django.db import models


class Todo(models.Model):
    name = models.CharField(max_length=250)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-updated"]
        
    def __str__(self):
        return self.name