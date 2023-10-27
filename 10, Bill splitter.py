# this is a bill splitter, useful when you're go out with friends and don't want to calculate serval times.

print("Welcome to the bill splitter")
total_bill = input("What was the total_bill? \n$")

percent_input = input("How much tip would you like to give? 5, 10, 12, 15?or any ammount\nPut '0' if you don't want to add any tip: ")

tip = int(percent_input) / 100

multipicationOfBill = float(total_bill) * float(tip)

total_sum = float(total_bill) + float(multipicationOfBill)

round_val = round(total_sum ,2)
print(round_val)

people = input("how many guys?: ")
print("so each one", round_val / int(people))
