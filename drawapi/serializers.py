from rest_framework import serializers
from drawapi.models import TeacherCoures

class TeacherCouresSerializer(serializers.ModelSerializer):
    class Meta:
        model=TeacherCoures
        fields=['id','teacher_name','course_name','course_duration','seat']