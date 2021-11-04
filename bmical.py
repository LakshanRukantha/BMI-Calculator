from os import system
from time import sleep

system('clear')
weight = float(input("Enter your weight in (KG) : "))
sleep(0.5)
height = float(input("Enter your height in (CM) : "))
height = float(height/100)
bmi = float(weight/height**2)
bmi = round(bmi)

sleep(1.0)
print("Calculating...")
sleep(1.5)
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