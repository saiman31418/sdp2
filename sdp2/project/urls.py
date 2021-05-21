from django.contrib.auth.views import LoginView

from . import views
from .views import *
from django.urls import path



urlpatterns=[

    path('',index,name='index'),
    path('register',register,name="register"),
    path('login',login,name="login"),
    path('appointment',appointment,name="appointment"),
    path("Admin",Admin,name="Admin"),
    path("AdminAppointments",AdminAppointments,name="AdminAppointments"),
    path("prescription",prescription,name="prescription"),
    path("doctoradvice",doctoradvice,name='doctoradvice'),
    path("Getadvice",Getadvice,name="Getadvice"),
    path('api', views.ChartData.as_view()),
    path('new', views.HomeView.as_view()),
    path("ambulance", ambulance, name="ambulance"),
    path("amb",amb,name="amb"),
    path("Doctor",Doctor,name="Doctor"),
    path("mp",mp,name="mp"),
    path("doctor_crud/<int:id>",doctor_crud,name="doctor_crud"),
    path("show",show,name="show"),
    path("home",home,name="home"),
    path("doctorname",doctorname,name="doctorname"),
    path("doctordashboard",doctordashboard,name="doctordashboard"),
    path("viewprofile/<int:id>",viewprofile,name="viewprofile"),
    path("viewdoctors",viewdoctors,name="viewdoctors"),
    path("doctorregister",doctorregister,name="doctorregister"),
    path("viewdoctors",viewdoctors,name="doctors"),
    path("check/<str:name>",check, name="check"),
    path("delete/<int:id>",delete,name="delete"),
    path("delaym",delaym,name='delaym'),
    path("statusv",statusv,name="statusv"),
    path("patientsdashboard",patientsdashboard,name="patientsdashboard"),
    path("medicalstore",medicalstore,name="medicalstore"),
    path("showcart/<int:id>",showcart,name="showcart"),
    path("deletecart/<int:id>",delelecart,name="deletecart"),
    path("payment",payment,name='payment'),
   path('ambulanceapi', views.AmbulanceData.as_view()),
    path('ambulancevis', views.Ambulancevis.as_view()),








]
