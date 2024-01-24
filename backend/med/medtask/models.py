from django.db import models
from django.contrib.auth.models import User

class medicalChartStatus(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    isActive = models.BooleanField(default=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.name)


class medicalChart(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    medicalChartStatus=models.ForeignKey(medicalChartStatus, on_delete=models.PROTECT)
    assignedTo=models.ForeignKey(User, blank=True, null=True, on_delete=models.PROTECT)
    isActive = models.BooleanField(default=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)



