from django.urls import path
from . import views

urlpatterns = [
    path('students/',views.Students,name='students'),
    path('profile/',views.Profile,name='profile'),
    path('viewappointments/<str:pk>/',views.ViewAppointments,name='viewappointments'),
]
