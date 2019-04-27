from django.db import models

# Subclass models.Model to create the new Job object
class Job(models.Model):
	image = models.ImageField(upload_to='images/')
	summary = models.CharField(max_length=200)
