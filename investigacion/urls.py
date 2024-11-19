from django.urls import path
from . import views

app_name= 'investigacion'
urlpatterns = [
    path('',views.index, name='index')
]