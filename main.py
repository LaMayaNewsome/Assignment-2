def getCategory(bmi):
  #Finds bmi category

  if bmi is None:
    return "Invalid Input"
    
  #Underweight <18.5
  if bmi < 18.5:
    return "Underweight"
  #Normal 18.5 - 24.9
  if 18.5 <= bmi < 25:
    return "Normal Weight"
  #Overweight 25 - 29.9
  if 25 <= bmi < 29.9:
    return "Overweight"
  #Obese >= 30
  else:
    return "Obese"


def calculateBMI(heightFeet, heightInches, weightPounds):
  
  #BMI calculator
  if heightFeet is None:
    heightFeet = int(input("Enter your height in feet: "))
  if heightInches is None:
    heightInches = int(input("Enter your height in inches: "))
  if weightPounds is None:
    weightPounds = int(
        input(
            "Enter your weight in pounds (round to the nearest whole number): "
        ))

  if heightFeet <= 0 or heightInches < 0 or weightPounds <= 0:
    return None

  #weightPounds X 0.45 = weight
  weight = weightPounds * 0.45
  #(heightFeet * 12 + height inches) x 0.025 = height
  heightSum = (heightFeet * 12 + heightInches) * 0.025
  #height x height = newHeight
  height = heightSum * heightSum
  #weight / height = bmi)
  bmiUnformatted = weight / height

  bmi = round(bmiUnformatted, 1)

  print("Your BMI is: ", bmi)
  print("Your BMI category is:", getCategory(bmi))
  return bmi


#Greet user and inform them about BMI calculator
print("Welcome to the BMI Calculator!")

#Output value and category
calculateBMI(heightFeet = None, heightInches = None, weightPounds = None)
#comment this out when testing