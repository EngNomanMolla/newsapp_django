from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .serializers import MyModelSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import MyModel

@api_view(['POST'])
def postnews(request):
    if request.method=='POST':
      serializer=  MyModelSerializer(data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(status=status.HTTP_201_CREATED,data=serializer.data)
      return Response(status=status.HTTP_404_NOT_FOUND,data={'response':'data not found'})
        

@api_view(['GET'])
def getnews(request):
    if request.method=='GET':
      data=  MyModel.objects.all()
      serialized_data = MyModelSerializer(data, many=True).data
      return Response(status=status.HTTP_200_OK,data=serialized_data)
    return Response(status=status.HTTP_404_NOT_FOUND,data={'response':'data not found'})


@api_view(['PUT'])
def updatenews(request,id):
     try:
         my_object = MyModel.objects.get(id=id)
     except MyModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
     serializer = MyModelSerializer(my_object, data=request.data)
     if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    
@api_view(['DELETE'])
def deletenews(request,id):
 if request.method=='DELETE':
    item = get_object_or_404(MyModel, id=id)
    item.delete()
    return Response(data={'data':'delete sucessfully'})
 return Response(data={'data':'something wrong'})
    
