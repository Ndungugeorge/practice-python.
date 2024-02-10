weight = float(input("Enter your weight in kg:"))
height = float(input("Enter tour height in meters:"))

bmi = round(weight / (height)**2)

if bmi<18.5:
    print(f"your bmi is {bmi} and you are underweight.")
elif bmi <25:
    print(f"your bmi is {bmi} and you are normal.")
elif bmi <30:
    print(f"your bmi is {bmi} and you are overweight.")
elif bmi <35:
    print(f"your bmi is {bmi} and you are obese.")
else:
    print(f"your bmi is {bmi} and you are clinically obese.")