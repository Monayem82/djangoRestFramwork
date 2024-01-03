from django.urls import path
from runapi import views
urlpatterns = [
    path('jsondata/',views.studenJsonView),
    path('jsondata/<int:st>',views.EachstudenJsonView),
]
