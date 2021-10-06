# Author: SMR (AMDG) 10/06/21
weight=float(input("What is your weight in kilograms?"))
height=float(input("What is your height in metres?"))
bmi= (weight)/(height**2)
if bmi>=40:
    print("You are Extremely Obese")
elif bmi>=30:
    print("You are Obese")
elif bmi>=25:
    print("You are Overweight")
elif bmi>=19:
    print("You are Healthy")
else:
    print("You are underweight")

