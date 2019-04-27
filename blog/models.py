from django.db import models

# Subclass models.Model to create the new Job object
class Blog(models.Model):
	image = models.ImageField(upload_to='images/')
	summary = models.CharField(max_length=400)
