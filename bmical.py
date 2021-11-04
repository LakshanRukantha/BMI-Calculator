from os import system
from time import sleep

system('clear')
weight = float(input("Enter your weight in (KG) : "))
if weight>700:
  print('='*50+"\nWeight can not acceptable!\n"+'='*50,'\n\n')
  exit();
sleep(0.5)
height = float(input("Enter your height in (CM) : "))
if height>300:
  print('='*50+"\nHeight can not acceptable!\n"+'='*50,'\n\n')
  exit();
height = float(height/100)
bmi = float(weight/height**2)
bmi = round(bmi)

sleep(1.0)
print('\n'+'='*50+"\nCalculating...\n"+'='*50,'\n')
sleep(1.5)
if bmi>=30:
  print('-'*50)
  print("Status : Obesity! \nBMI Index :",bmi)
  print('-'*50)
elif bmi>=25 and bmi<=30:
  print('-'*50)
  print("Status : Overweight! \nBMI Index :",bmi)
  print('-'*50)
elif bmi>=20 and bmi<=25:
  print('-'*50)
  print("Status : Normal Weight! \nBMI Index :",bmi)
  print('-'*50)
else:
  print('-'*50)
  print("Status : Underweight! \nBMI Index :",bmi)
  print('-'*50)