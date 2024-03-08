import pytest
from main import calculateBMI, getCategory

#Test cases for calculate_bmi function
def test_bmiCalculation():
  assert calculateBMI(5, 9, 160), pytest.approx(23.6, abs=0.1) 
  
def test_bmiBoundaryShift():
  assert calculateBMI(5, 9, 140), pytest.approx(18.5, abs=0.1)
  assert calculateBMI(5, 9, 141), pytest.approx(18.4, abs = 0.1)
  
def test_invalid():
  assert calculateBMI(0, 0, 0) == None #Invalid input


#Test cases for get_bmi_category
def test_underWeight():
  assert getCategory(5.9) == "Underweight"
  
def test_normalWeight():
  assert getCategory(21) == "Normal Weight"
  
def test_overWeight():
  assert getCategory(28) == "Overweight"
  
def test_obese():
  assert getCategory(31) == "Obese"

def test_categoryBoundaryShift():
  assert getCategory(18.5) == "Normal Weight"
  assert getCategory(18.4) == "Underweight"
