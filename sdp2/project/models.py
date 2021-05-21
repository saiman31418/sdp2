from django.db import models
from datetime import date

# Create your models here.
from spyder.Scripts.runxlrd import options


class User(models.Model):
		# fields of the model

        Username = models.CharField(max_length=40)

        email = models.CharField(max_length=50, unique=True)
        phone = models.CharField(max_length=30)
        pass1 = models.CharField(max_length=200)

class Appointment(models.Model):
    selectlocation=models.CharField(max_length=20, choices=(("viajayawada", "vijawada"), ("hyderabad", "hyderabad")),
                                      default="select location")
    selectdepartment=models.CharField(max_length=30,
                                        choices=(("cardio", "cardio"), ("neuro", "neuro"), ("gastro", "gastro")),
                                        default="selectdepartment")
    patientname=models.CharField(max_length=30)
    patientmobile=models.CharField(max_length=30)
    patientEmail=models.CharField(max_length=30)
    doctor=models.CharField(max_length=40,
                                        choices=(("k.jayasurya", "k.jayasurya"), ("b.padmanabhasimha", "b.padmanabhasimha")),
                                        default="doctor")
    datetime=models.DateField(auto_now_add=True,auto_now=False,blank=True)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    previoushealthrecord = models.CharField(max_length=60,default="asthama")
    previousmedication=models.CharField(max_length=60,default="diabetic")











class Prescription(models.Model):
     patientname=models.CharField(max_length=40)
     symptoms=models.CharField(max_length=40)

     def __str__(self):
         return self.patientname +"/"+ self.symptoms
class Ambulance(models.Model):
    name=models.CharField(max_length=30)
    phonenumber=models.CharField(max_length=30)
    location=models.CharField(max_length=30)

    def test_add(self):
        return self.name






class DoctorAdvice(models.Model):
    patientname=models.ForeignKey(Prescription,on_delete=models.CASCADE)

    remedy=models.CharField(max_length=40)
class Doctorregister(models.Model):
    name=models.CharField(max_length=40)
    specialization=models.CharField(max_length=40)
    maxappointments=models.IntegerField()
    password=models.CharField(max_length=8)
    email=models.CharField(max_length=40,default="abcd@gmail.com")
    phone=models.CharField(max_length=40,default="12345678")
class status(models.Model):
    doctorname=models.ForeignKey(Doctorregister,on_delete=models.CASCADE)
    filled=models.IntegerField()
class delay(models.Model):
    patientname=models.CharField(max_length=40)
    patientstatus=models.CharField(max_length=40,default="waiting")

    datetime = models.DateField(auto_now_add=True, auto_now=False, blank=True)
class cart(models.Model):
    medicinename=models.CharField(max_length=40)
    medicineuse=models.CharField(max_length=40)
    images=models.ImageField(upload_to='cartimg/')
    price=models.IntegerField()
class Showcart(models.Model):
    name=models.CharField(max_length=40)
    price=models.IntegerField()














