from datetime import datetime

from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import message
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse, request
from .forms import UserForm, patientAppointment, PrescriptionForm, DoctorAdviceForm, AmbulanceForm, DoctorregisterForm, \
   delayForm
from .models import Appointment, Prescription, DoctorAdvice, Ambulance, Doctorregister, status, delay, cart, Showcart
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import View
from .models import User
from django.core.mail import send_mail
from  sdp2 import settings
import pulp as p
from datetime import date
# Create your views here.
def index(request):
   return  render(request,"index.html")
def register(request):
   if request.method == "POST":

     form=UserForm(request.POST)
     if form.is_valid():

        form.save()
        return render(request,"login.html")

     else:
        return HttpResponse("invalid")

   else:
      form=UserForm()


   return render(request, 'register.html',{"form":form})







def login(request):
   if request.method == 'POST':
      username=request.POST["username"]
      pass1=request.POST["pass1"]
      #user=auth.authenticate(username=username,password=pass1)
      ex=User.objects.get(Username=username)

      if username==ex.Username and pass1==ex.pass1:
         return render(request,"home.html")




      else:
         return HttpResponse("invalid")






   else:
      return render(request,"login.html")
def home(request):
   return render("home.html")
def appointment(request):

   if request.method=='POST':
      c = list(status.objects.filter(doctorname_id__in=(1,2)))
      if c[0].filled>9 or c[1].filled>9:

            return render(request,"delay.html")

      appointmentform = patientAppointment(request.POST)





      if appointmentform.is_valid():
         appointmentform.save()
         return render(request,"home.html")
      else:
         return HttpResponse("invalid")
   else:
      appointmentform = patientAppointment()

   return render(request,"appointment.html",{"appointmentform":appointmentform})

def Admin(request):
   if request.method == 'POST':
      username=request.POST["username"]
      pass1=request.POST["pass1"]
      user=auth.authenticate(username=username,password=pass1)
      if user is not None:
         auth.login(request,user)
         return render(request,"adminhome.html")

      else:
         print("invalid")








   else:
      return render(request,"admin.html")
def AdminAppointments(request):
   today = date.today()
   d2 = today.strftime("%y-%m-%d")
   ap=Appointment.objects.raw("select id from project_appointment where datetime='"+d2+"'")

   return render(request,"adminpage.html",{"ap":ap})
def prescription(request):
   if request.method == 'POST':
      prescriptionform = PrescriptionForm(request.POST)
      if prescriptionform.is_valid():
         prescriptionform.save()
      else:
         return HttpResponse("invalid")
   else:
      prescriptionform = PrescriptionForm()

   return render(request, "prescription.html", {"prescriptionform": prescriptionform})
def doctoradvice(request):
   if request.method == 'POST':
      doctoradvice = DoctorAdviceForm()
      patient = Prescription.objects.all()
      new=DoctorAdvice.objects.all()
      context = {
         "patient": patient,
         "doctoradvice": doctoradvice,
         "new":new
      }
      doctoradvice = DoctorAdviceForm(request.POST)
      if doctoradvice.is_valid():
         doctoradvice.save()
      else:
         return HttpResponse("invalid")
   else:
         doctoradvice= DoctorAdviceForm()
         patient=Prescription.objects.all()
         context={
            "patient": patient,
            "doctoradvice":doctoradvice }
   return render(request, "doctoradvice.html",  context)
def Getadvice(request):
   da= DoctorAdvice.objects.all()
   return  render(request,"getadvice.html",{"da":da})


class HomeView(View):
   def get(self, request, *args, **kwargs):
      return render(request, 'ds.html')


class ChartData(APIView):
   authentication_classes = []
   permission_classes = []


   def get(self, request, format=None):
      a = 0
      labels = []
      chartLabel = "my data"
      chartdata = []
      emp = Prescription.objects.all()
      for i in emp:
         if i.symptoms in labels:
            continue
         else:
            labels.append(i.symptoms)
            a=Prescription.objects.filter(symptoms=i.symptoms).count()
            chartdata.append(a)

      print(chartdata)

      data = {
         "labels": labels,
         "chartLabel": chartLabel,
         "chartdata": chartdata,
      }
      return Response(data)
def ambulance(request):
   res=0
   if request.method == "POST":

     form=AmbulanceForm(request.POST)
     if form.is_valid():
        obj=Ambulance.objects.all()
        for i in obj:
           subject = "alert!!!!"
           msg = "name:" + i.name +"\n"+ "location" + i.location+ "\n"+"phone" + i.phonenumber + ""
           to = "bharathcherukuri00@gmail.com"
           res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
        if (res == 1):
           msg = "Mail Sent" + i.name+ " Successfuly "
        else:
           msg = "Mail could not sent"



        form.save()



     else:
        return HttpResponse("invalid")

   else:
      form=AmbulanceForm()


   return render(request, 'ambulance.html',{"form":form})
def amb(request):

      form=AmbulanceForm()


      return render(request, 'ambulance.html',{"form":form})
def Doctor(request):
   if request.method == 'POST':
      name=request.POST["username"]
      password=request.POST["pass1"]

      ex = Doctorregister.objects.get(name=name)

      if name == ex.name and password == ex.password:
            return render(request, "doctoradvice.html")
      else:
         return HttpResponse("invalid")








   else:
      return render(request,"doctor.html")
def mp(request):
   if request.method == 'POST':
      online=request.POST["online"]
      offline=request.POST["offline"]
      max=request.POST["max"]
      off=request.POST["off"]
      mino=request.POST["mino"]
      maxoff=request.POST["maxoff"]





      Lp_prob = p.LpProblem('Problem', p.LpMinimize)


      x = p.LpVariable("x", lowBound=0)
      y = p.LpVariable("y", lowBound=0)

      # Objective Function #100 #150
      Lp_prob += int(online)* x + 150 * int(offline)

      # Constraints:
      Lp_prob += x +  y >= int(max) #70
      Lp_prob += x - y >= int(off)   #10
      Lp_prob += x <= int(mino)             #10
      Lp_prob += y >= int(maxoff)            #50


      print(Lp_prob)

      status = Lp_prob.solve()
      print(p.LpStatus[status])


      print(p.value(x), p.value(y), p.value(Lp_prob.objective))
      return JsonResponse(
         {"total profit":p.value(Lp_prob.objective)}






      )
   return render(request,"mp.html")

def doctor_crud(request,id):
   employee = DoctorAdvice.objects.get(id=id)
   form = DoctorAdviceForm(request.POST,instance=employee)
   if form.is_valid():
      form.save()
      return redirect("doctoradvice")
   return render(request, 'edit.html', {'employee': employee})
def show(request):
   if request.method == 'POST':
      doctoradvice = DoctorAdviceForm()
      patient = Prescription.objects.all()
      new=DoctorAdvice.objects.all()
      context = {
         "patient": patient,
         "doctoradvice": doctoradvice,
         "new":new
      }
      doctoradvice = DoctorAdviceForm(request.POST)
      if doctoradvice.is_valid():
         doctoradvice.save()
      else:
         return HttpResponse("invalid")
   else:
         doctoradvice= DoctorAdvice.objects.all()
         patient=Prescription.objects.all()
         context={
            "patient": patient,
            "doctoradvice":doctoradvice }
   return render(request, "new.html",  context)

def doctorname(request):
   return render(request,"doctorname.html")
def doctordashboard(request):
   if request.method == 'POST':
      name=request.POST["name"]
      today = date.today()
      d2 = today.strftime("%y-%m-%d")
      ex=Appointment.objects.raw("select id from project_Appointment where datetime='"+d2+"' and doctor='"+name+"' ")
   return render(request,"doctordashboard.html",{'ex':ex})
def viewprofile(request,id):
   i=Appointment.objects.get(id=id)
   return render(request,"profile.html",{"i":i})

def doctorregister(request):
   if request.method == "POST":

     form=DoctorregisterForm(request.POST)
     if form.is_valid():

        form.save()
        return render(request,"doctor.html")

     else:
        return HttpResponse("invalid")

   else:
      form=DoctorregisterForm()


   return render(request, 'doctorregister.html',{"form":form})
def viewdoctors(request):
   today = date.today()
   d2 = today.strftime("%y-%m-%d")
   dname=Doctorregister.objects.all()
   c=0

   for i in dname:
      ex=Appointment.objects.raw("select id from project_Appointment where datetime='"+d2+"' and doctor='"+i.name+"' ")
      for j in ex:
         c=c+1
      p=status(doctorname=i,filled=c)
      p.save()

      print(c)
      c=0
      new=Doctorregister.objects.all()
      for i in new:
         for row in status.objects.all().reverse():
            if status.objects.filter(doctorname=i).count() > 1:
               row.delete()




   return render(request,"newprofile.html",{"ex":status.objects.raw("select distinct * from project_status")})



def check(request,name):
   new=Doctorregister.objects.get(name=name)

   new1=status.objects.get(name=new)

   for j in new1:
      if j.count<10:

         form = patientAppointment(request.POST)
         if form.is_valid():
            form.save()
            return redirect("doctor")
      else:
         return HttpResponse("appointments are filled ")
      appointmentform=patientAppointment()

   return render(request,"appointment.html",{"appointmentform":appointmentform})
def delete(request,id):
   new=Appointment.objects.get(id=id)
   new.delete()
   return  redirect("doctordashboard")
def delaym(request):
   if request.method == 'POST':
      name=request.POST["name"]
      doctorname=request.POST["doctor"]


      p=delay(patientname=name,patientstatus="waiting")
      p.save()
      ex=Doctorregister.objects.get(name=doctorname)
      b=status.objects.get(doctorname=ex)
      f=b.filled
      a=status.objects.filter(doctorname=ex).update(filled=f+1)




   return render(request,"delay.html",{"ex": delay.objects.all()} )
def patientsdashboard(request):
   today = date.today()
   d2 = today.strftime("%y-%m-%d")
   ex=delay.objects.raw("select id from project_delay where datetime='"+d2+"'  ")

   c=0
   for i in ex:
      c=c+1

   ex1 = status.objects.raw("update table project_status set filled=10-c")
   return render(request,"patientsdashboard.html",{'ex':ex})

def statusv(request):
   ex=status.objects.raw("select id from project_status")
   return  render(request,"newprofile.html",{"ex":ex})
def medicalstore(request):
   ex=cart.objects.all()
   return render(request,"ex.html",{"ex":ex})


def showcart(request,id):
      ex=cart.objects.get(id=id)

      name=ex.medicinename
      price=ex.price
      new=Showcart(name=name,price=price)
      new.save()
      new1=Showcart.objects.all()
      return render(request,"cart.html",{"new1":new1})



def delelecart(request,id):
   ex=Showcart.objects.get(id=id)
   ex.delete()
   new1 = Showcart.objects.all()

   return render(request,"newcart.html",{"new1":new1})
def payment(request):
   ex=Showcart.objects.all()
   sum=0
   for i in ex:
      sum=sum+i.price
   return render(request,"payment.html",{"price":sum})


class Ambulancevis(View):
   def get(self, request, *args, **kwargs):
      return render(request, 'ambulancevis.html')


class AmbulanceData(APIView):
   authentication_classes = []
   permission_classes = []

   def get(self, request, format=None):
      labels = [

      ]
      chartLabel = "my data"
      chartdata = []
      ex=Ambulance.objects.all()
      for i in ex:
         if i.location in labels:
            continue
         else:
            labels.append(i.location)
            a = Ambulance.objects.filter(location=i.location).count()

            chartdata.append(a)
      data = {
         "labels": labels,
         "chartLabel": chartLabel,
         "chartdata": chartdata,
      }
      return Response(data)
























