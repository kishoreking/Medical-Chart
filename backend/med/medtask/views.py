from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User

class medicalChartInfoGetApi(APIView):

    def get(self,request):
        d=medicalChart.objects.filter().order_by("id")
        biS=medicalChartSerializer001(d,many=True)
        resultMain=biS.data
        return Response(resultMain, status=200)
    
    def post(self,request):
        pass

class medicalCharAllocatedUserInfoGetApi(APIView):

    def get(self,request):
        result=[]
        users=User.objects.filter(is_superuser=False).order_by("id")
        for u in users:
            d=medicalChart.objects.filter(assignedTo=u).order_by("id")
            biS=medicalChartSerializer001(d,many=True) 
            r={}
            r["id"]=u.id
            r["user"]=u.username
            r["charts"]=biS.data
            result.append(r)         
        return Response(result, status=200)
    
    def post(self,request):
        pass

class medicalChartChangeStatus(APIView):

    def get(self,request):
        
        data0=request.data
        
        print(";;;;;",data0)
        id=data0["id"]
        status=data0["status"]
        obj=medicalChart.objects.filter(id=id).update(medicalChartStatus=status)
        obj2=medicalChart.objects.filter(id=id).first()
        obj3=medicalChart.objects.filter(assignedTo=obj2.assignedTo).filter(medicalChartStatus=2)
        if obj3.count()<10:
            mc=medicalChart.objects.filter(medicalChartStatus=1).first()
            if mc:
                mc.medicalChartStatus_id=2
                mc.assignedTo=obj2.assignedTo
                mc.save()

        return Response("Success",status=200)        
        
    def post(self,request):
        pass
    
class medicalChartStatusReset(APIView):

    def get(self,request):
        pass

    def post(self,request):
        obj=medicalChart.objects.all().update(medicalChartStatus=1, assignedTo=None)
        return Response("Success",status=200)        

class firstTimeAssingment(APIView):

    def get(self,request):
        pass

    def post(self, request):
        maxchartsperuser = 10
        users = User.objects.filter(is_superuser=False)
        totalusers = len(users)
        numchartsperuser=maxchartsperuser*totalusers
        x=medicalChartStatus.objects.filter(id=2).first()
        charts = medicalChart.objects.filter(assignedTo=None).order_by('id')
        for i, chart in enumerate(charts):
            userindex = i % totalusers
            user = users[userindex]
            obj3=medicalChart.objects.filter(assignedTo=user).filter(medicalChartStatus=2)
            if obj3.count()<10:   
                chart.assignedTo = user
                chart.medicalChartStatus = x                         
                chart.save()
            if (i + 1) % numchartsperuser == 0:
                break

        return Response("Success", status=200)
   