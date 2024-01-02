from django.shortcuts import render
from drawapi.models import TeacherCoures
from drawapi.serializers import TeacherCouresSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Create your views here.
# sqlset
def tcoursView(request):
    # complex data
    tcs=TeacherCoures.objects.all()
    # Creating a Dictionary 
    serializer=TeacherCouresSerializer(tcs,many=True)
    # render a JSon data
    json_data=JSONRenderer().render(serializer.data)
    
    return HttpResponse(json_data,content_type='application/json')

def tcoursView_ins(request,pk):
    # complex data
    tcs=TeacherCoures.objects.get(id=pk)
    # Creating a Dictionary 
    serializer=TeacherCouresSerializer(tcs)
    # render a JSon data ===
    json_data=JSONRenderer().render(serializer.data)
    
    return HttpResponse(json_data,content_type='application/json')


