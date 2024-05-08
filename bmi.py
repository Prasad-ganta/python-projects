weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)

if bmi < 18.5:
    a= "Underweight"
elif 18.5 <= bmi < 24.9:
    a = "Normal weight"
elif 24.9 <= bmi < 29.9:
    a = "Overweight"
else:
    a= "Obese"
    
print(f"Your BMI is {bmi:.2f}. This is considered {a}.")