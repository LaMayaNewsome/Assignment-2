import pytest
from BMI import calculateBMI, getCategory

def test_calculateBMI(self):
    #Test cases for calculate_bmi function
    assert calculateBMI(5, 9, 160), pytest.approx(23.6, abs=0.1) #Normal weight
    assert calculateBMI(6, 0, 200), pytest.approx(27.1, abs=0.1) #Overweight
    assert calculateBMI(0, 0, 0) #Invalid input

def test_getCategory(self):
    #Test cases for get_bmi_category
    assert getCategory(21) == "Underweight"
    assert getCategory(21) == "Normal weight"
    assert getCategory(27) == "Overweight"
    assert getCategory(21) == "Obese"
    assert getCategory(None) == "Invalid Innput"

    
    