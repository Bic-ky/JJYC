# models.py

from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError

class Projects(models.Model):
    STATUS_CHOICES = [
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
    ]

    title = models.CharField(max_length=255)
    working_areas = models.TextField(blank=True)
    total_budget = models.DecimalField(max_digits=10, decimal_places=2) 
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ongoing')

    photos = models.ImageField(upload_to='photos/')
    videos = models.FileField(upload_to='media/videos/' , blank=True)
    description = models.TextField(blank=True)
    partners = models.CharField(max_length=255)
    partners_logo = models.ImageField(upload_to='media/logos/')
    project_documents = models.FileField(upload_to='media/Project/documents/', blank=True, null=True)
    url = models.URLField(blank=True)

    is_completed = models.BooleanField(default=False)

    upload_date = models.DateTimeField(auto_now_add=True)
    starting_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title

