from django.urls import path
from drawapi import views
urlpatterns = [
    path('jsonView/',views.tcoursView),
]
