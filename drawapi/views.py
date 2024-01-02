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

    serializer=TeacherCouresSerializer(tcs,many=True)

    json_data=JSONRenderer().render(serializer.data)
    
    return HttpResponse(json_data,content_type='application/json')


