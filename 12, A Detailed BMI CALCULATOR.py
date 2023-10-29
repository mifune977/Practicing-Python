height = float(input("What's your height in meter: \n"))
weight = float(input("What's your weight in kg: \n"))

bmi = (weight / (height ** 2))

if bmi <= 18.5:
    print(f"Your BMI is {bmi:.0f}, currently you are \033[1munderweight")
elif 18.5 < bmi <25:
    print(f"Your BMI is {bmi:.0f}, currently you have a \033[1mnormal weight.")
elif 25 < bmi < 30:
    print(f"Your BMI is {bmi:.0f}, currently you are slightly \033[1moverweight.")
elif 30 < bmi < 35:
    print(f"Your BMI is {bmi:.0f}, currently you are \033[1mobese.")
elif 35 < bmi:
    print(f"Your BMI is {bmi:.0f}, currently you are \033[1mclinically obese.")

########for bold text = '\033[1m'########
