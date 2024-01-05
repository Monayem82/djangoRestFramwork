from django.urls import path
from drawapi import views
urlpatterns = [
    path('teacherCreate/',views.teacherCoursCreateView),
    path('teacherCreate/<int:pk>',views.teacherCoursCreateView),


    # path('jsonView/',views.tcoursView),
    # path('jsonView/<int:pk>/',views.tcoursView_ins),
    # path('createde/',views.tcours_Create_DeserializeView),
]
