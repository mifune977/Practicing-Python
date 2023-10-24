height = input("What's your height in meter: \n")
weight = input("What's your weight in kg: \n")

w = float(weight)
h = float(height)

print("your BMI value is: \n" + str(round(w/(h**2), 2)))
