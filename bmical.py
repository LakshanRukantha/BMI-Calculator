import os

weight = float(input("Enter your weight in (KG) : "))
height = float(input("Enter your height in (CM) : "))
height = float(height/100)
bmi = float(weight/height**2)
bmi = round(bmi)

print("Your BMI is : ",bmi)