from django.db import models

class TeacherCoures(models.Model):
    teacher_name=models.CharField(max_length=25)
    course_name=models.CharField(max_length=30)
    course_duration=models.IntegerField()
    seat=models.IntegerField()
