from django.db import models

# Create your models here.
class AC_DICT(models.Model):
	abbreviation = models.CharField(max_length=20)
	full_form = models.CharField(max_length=255)