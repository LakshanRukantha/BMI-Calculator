import os

weight = float(input("Enter your weight in (KG) : "))
height = float(input("Enter your height in (CM) : "))
height = float(height/100)
bmi = float(weight/height**2)
bmi = round(bmi)

if bmi>=30:
  print("You are Obesity!")
  print("Your BMI is :",bmi)
elif bmi>=25 and bmi<=30:
  print("You are Overweight!")
  print("Your BMI is :",bmi)
elif bmi>=20 and bmi<=25:
  print("You are Normal Weight!")
  print("Your BMI is :",bmi)
else:
  print("You are Underweight!")
  print("Your BMI is :",bmi)