from django.urls import path
from supers import views

urlpatterns = [
    path('', views.supers_list)

]