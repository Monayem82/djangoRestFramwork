from django.shortcuts import render
from drawapi.models import TeacherCoures
from drawapi.serializers import TeacherCouresSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser


# api_view in GET operations 
@api_view(['GET','POST','PUT','PATCH','DELETE'])
def teacherCoursCreateView(request,pk=None):
    if request.method=="GET":
        id=pk
        if id is not None:
            # complex data 
            tdata=TeacherCoures.objects.get(id=id)
            # pythn data
            serializer=TeacherCouresSerializer(tdata)
            return Response(serializer.data)

        else:
            tdata=TeacherCoures.objects.all()
            serializer=TeacherCouresSerializer(tdata,many=True)
            return Response(serializer.data)

    if request.method=='POST':
        serializer=TeacherCouresSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res={"smg":"Successfully data insert"}
            return Response(res)
        return Response(serializer.errors)


    if request.method=="PUT":
        id=pk
        tdatas=TeacherCoures.objects.get(id=id)
        seriliz=TeacherCouresSerializer(tdatas,data=request.data)
        if seriliz.is_valid():
            seriliz.save()
            return Response({"res":"insert PUT"})
        return Response(seriliz.errors)
    
    if request.method=="PATCH":
        id=pk
        tdatas=TeacherCoures.objects.get(id=id)
        seriliz=TeacherCouresSerializer(tdatas,data=request.data,partial=True)
        if seriliz.is_valid():
            seriliz.save()
            return Response({"res":"insert PATCH"})
        return Response(seriliz.errors)
    
    if request.method=='DELETE':
        id=pk
        tdata_d=TeacherCoures.objects.get(id=id)
        tdata_d.delete()
        return Response({"res":"Successfully data delete"})



# sqlset
# def tcoursView(request):
#     # complex data
#     tcs=TeacherCoures.objects.all()
#     # Creating a Dictionary 
#     serializer=TeacherCouresSerializer(tcs,many=True)
#     # render a JSon data
#     json_data=JSONRenderer().render(serializer.data)
    
#     return HttpResponse(json_data,content_type='application/json')

# def tcoursView_ins(request,pk):
#     # complex data
#     tcs=TeacherCoures.objects.get(id=pk)
#     # Creating a Dictionary 
#     serializer=TeacherCouresSerializer(tcs)
#     # render a JSon data =
#     json_data=JSONRenderer().render(serializer.data)
    
#     return HttpResponse(json_data,content_type='application/json')

# @csrf_exempt
# def tcours_Create_DeserializeView(request):
#     if request.method=='POST':
#         json_data=request.body
#         # json to stream convert
#         stram=io.BytesIO(json_data)
#         # Stream to python 
#         pythonData=JSONParser().parse(stram)
#         #python complex data 
#         serializer=TeacherCouresSerializer(data=pythonData)
#         if serializer.is_valid():
#             serializer.save()
#             res={"msg":"Data insert successfully"}
#             json_data=JSONRenderer().render(res)
#             return HttpResponse(json_data,content_type='application/json')   
#         else:
#             json_data=JSONRenderer().render(serializer.errors)
#             return HttpResponse(json_data,content_type='application/json')

