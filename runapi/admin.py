from django.contrib import admin
from runapi.models import studentModel

@admin.register(studentModel)
class studentModelAdmin(admin.ModelAdmin):
    list_display=('id','student_name','department','roll','batch')