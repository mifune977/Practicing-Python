height = input("What's your height in meter: ")
weight = input("What's your weight in kg: ")

w = float(weight)
h = float(height)

print("your BMI value is: " + str(w/(h**2)))
