from django.contrib import admin
from .models import *



# Register your models here.

# for i in range(2,151):
#     s=medicalChartStatus.objects.filter(id=1).first()
#     cn=f"Chart{i}"
#     c=medicalChart.objects.create(name=cn,medicalChartStatus=s)
#     pass

# a=medicalChart.objects.filter().update(medicalChartStatus=1)
# a=medicalChart.objects.filter(id__gt=150).delete()
class medicalChartStatusAdmin(admin.ModelAdmin):
    list_display=("id","name","isActive", "modified_at", "created_at")
admin.site.register(medicalChartStatus, medicalChartStatusAdmin)

class medicalChartAdmin(admin.ModelAdmin):
    list_display=("id","name", "medicalChartStatus","assignedTo","isActive", "modified_at", "created_at")
admin.site.register(medicalChart, medicalChartAdmin)
