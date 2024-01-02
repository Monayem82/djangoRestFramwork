from rest_framework import serializers

class TeacherCouresSerializer(serializers.Serializer):
    teacher_name=serializers.CharField(max_length=25)
    course_name=serializers.CharField(max_length=30)
    course_duration=serializers.IntegerField()
    seat=serializers.IntegerField()