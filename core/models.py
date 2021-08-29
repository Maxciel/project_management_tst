#from typing_extensions import Required
from django.db import models

# Create your models here.

class Project(models.Model):
    PRIORITIES = (
        (0, 'Baixo'),
        (1, 'Médio'),
        (2, 'Alto')
    )
    project_name = models.CharField(max_length=200, null=False, blank=False)
    start_date = models.DateField(null=False, blank=False)
    finish_date = models.DateField(null=False, blank=False)
    proj_amount = models.DecimalField(max_digits=14, decimal_places=2, null=False, blank=False)
    proj_risk = models.IntegerField(null=False, blank=False, default=0, choices=PRIORITIES)
    proj_team = models.TextField(max_length=255)
    