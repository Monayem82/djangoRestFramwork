from django.contrib import admin
from drawapi.models import TeacherCoures
# Register your models here.

@admin.register(TeacherCoures)
class TeacharCourse(admin.ModelAdmin):
    list_display=['id','teacher_name','course_name','course_duration','seat']