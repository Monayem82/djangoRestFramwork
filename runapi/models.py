from django.db import models

class studentModel(models.Model):
    student_name=models.CharField(max_length=30)
    department=models.CharField(max_length=3)
    roll=models.IntegerField()
    batch=models.CharField(max_length=7)
