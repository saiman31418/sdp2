import pytest
from django.test import TestCase
from project.models import *

def test_add(self):
      c=Ambulance.objects.get(name="rajkumar")
      assert c.name=="rajkumar"