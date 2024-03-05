from django.shortcuts import render

# Create your views here.

from app.serializers import *
from app.models import *

from rest_framework.decorators import APIView

from rest_framework.response import Response

class ProductCrud(APIView):
    def get(self,request,id):
        POD=Product.objects.all()   #orm
        JOD=ProductModelSerializer(POD,many=True)     #json
        # POD=Product.objects.get(id=id)
        # JOD=ProductModelSerializer(data=POD)           #json
        return Response(JOD.data)
    
    def post(self,request,id):
        JDO=request.data
        PDO=ProductModelSerializer(data=JDO)
        if PDO.is_valid():
            PDO.save()
            return Response({'insert':'Data is inserted Successfully'})
        else:
            return Response({'Error':'Data is not Inserted'})
        
    def put(self,request,id):
        PO=Product.objects.get(id=id)
        UPDO=ProductModelSerializer(PO,data=request.data)
        if UPDO.is_valid():
            UPDO.save()
            return Response({'update':'Data is Updated'})
        else:
            return Response({'error':'Update not done'})
        
    def patch(self,request,id):
        PO=Product.objects.get(id=id)
        UPDO=ProductModelSerializer(PO,data=request.data,partial=True)
        if UPDO.is_valid():
            UPDO.save()
            return Response({'update':'Data is Updated'})
        else:
            return Response({'error':'Update not done'})
        
    def delete(self,request,id):
        Product.objects.get(id=id).delete()
        return Response({'deletion':'Data is Deleted'})
