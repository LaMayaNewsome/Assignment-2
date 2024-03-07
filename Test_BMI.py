import unittest
from BMI import calculateBMI, getCategory

class TestBMICalculator(unittest.Testcase):
    def test_calculateBMI(self):
        #Test cases for calculate_bmi function
        self.assertAlmostEqual(calculateBMI(5, 9, 160), 23.6, places=1) #Normal weight
        self.assertAlmostEqual(calculateBMI(6, 0, 200), 27.1, places=1) #Overweight
        self.assertIsNone(calculateBMI(0, 0, 0)) #Invalid input

    def test_getCategory(self):
        #Test cases for get_bmi_category
        self.assertEqual(getCategory(21), "Underweight")
        self.assertEqual(getCategory(21), "Normal weight")
        self.assertEqual(getCategory(27), "Overweight")
        self.assertEqual(getCategory(21), "Obese")
        self.assertEqual(getCategory(None), "Invalid Innput")

    if __name__ == "__main__":
        unittest.main()

    