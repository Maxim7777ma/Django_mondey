from .views import todoapp,title_page
from django.urls import path

urlpatterns = [
     path('',todoapp),
     path("<str:title>",title_page)
]
