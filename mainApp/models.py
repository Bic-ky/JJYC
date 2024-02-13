from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, role=None):
        if not phone_number:
            raise ValueError('The Phone Number field must be set')

        user = self.model(phone_number=phone_number, role=role)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, phone_number, password=None):
        # Create and save a new superuser with the given phone number and password
        user = self.create_user(phone_number, password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



class Projects(models.Model):
    STATUS_CHOICES = [
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
    ]

    title = models.CharField(max_length=255)
    working_areas = models.TextField(blank=True)
    total_budget = models.DecimalField(max_digits=10, decimal_places=2) 
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ongoing')

    photos = models.ImageField(upload_to='Project/photos')
    videos = models.FileField(upload_to='Project/videos' , blank=True)
    description = models.TextField(blank=True)
    partners = models.CharField(max_length=255)
    partners_logo = models.ImageField(upload_to='Partner/logos')
    project_document = models.FileField(upload_to='Project/documents', blank=True, null=True)
    url = models.URLField(blank=True)

    is_completed = models.BooleanField(default=False)

    upload_date = models.DateTimeField(auto_now_add=True)
    starting_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title

    def get_duration(self):
        # Calculate the difference between end_date and starting_date
        duration = self.end_date - self.starting_date

        # Convert the duration to months
        months = duration.days // 30  # Assuming an average month has 30 days

        return months
    


class Announcement(models.Model):
    image = models.ImageField(upload_to='Announcements/image')
    title = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='Announcements/files/', blank=True, null=True)
    url = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.title