from django.shortcuts import render
from runapi.serializers import studentModelSerializer
from runapi.models import studentModel
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse


def studenJsonView(request):
    stdapi=studentModel.objects.all()
    serializer=studentModelSerializer(stdapi,many=True)
    json_data=JSONRenderer().render(serializer.data)

    return HttpResponse(json_data,content_type='application/json')

def EachstudenJsonView(request,st):
    stdapi=studentModel.objects.get(id=st)
    serializer=studentModelSerializer(stdapi)
    json_data=JSONRenderer().render(serializer.data)

    return HttpResponse(json_data,content_type='application/json')


