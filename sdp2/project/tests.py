from django.test import TestCase

# Create your tests here.
from .models import Prescription, Ambulance
import pytest





class Ambulance_test(TestCase):
    def set_up(self):

       b=Ambulance.objects.create(name="rajkumar",location="vij",phonenumber="1234567")
       b.save




    def test_add(self):
        c = Ambulance.objects.get(name="rajkumar")


        assert c.name=="rajkumar"









