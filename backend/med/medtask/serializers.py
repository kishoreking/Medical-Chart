from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
class Dropdown_Field(serializers.Field):
    def to_representation(self, value):
        returnValueOnError = {"id":value.medicalChartStatus.id, "name":""}
        try:
            b=medicalChartStatus.objects.filter(id=value.medicalChartStatus.id).first()
            if b is None:
                return returnValueOnError
        except medicalChartStatus.DoesNotExist:
            return returnValueOnError
        return {"id":value.medicalChartStatus.id, "name":b.name}
    
class Modified_byField(serializers.Field):
    def to_representation(self, value):
        if value.assignedTo==None:
            return {"id":value.assignedTo, "first_name":"", "last_name":"", "name":""}
            
        returnValueOnError = {"id":value.assignedTo.id, "first_name":"", "last_name":"", "name":""}
        try:
            b=User.objects.filter(id=value.assignedTo.id).first()
            if b is None:
                return returnValueOnError
        except User.DoesNotExist:
            return returnValueOnError
        return {"id":value.assignedTo.id, "first_name":b.first_name, "last_name":b.last_name,"name":b.username}    

class medicalChartSerializer001(serializers.ModelSerializer):
    medicalChartStatus= Dropdown_Field(source="*")
    assignedTo=Modified_byField(source="*")

    class Meta:
        model = medicalChart
        fields = "__all__"

    