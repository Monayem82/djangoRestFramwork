from rest_framework import serializers

class studentModelSerializer(serializers.Serializer):
    student_name=serializers.CharField(max_length=30)
    department=serializers.CharField(max_length=3)
    roll=serializers.IntegerField()
    batch=serializers.CharField(max_length=7)