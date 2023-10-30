year = int(input("Check Leap year or Not?\n"))

if (year % 400 == 0) and (year % 100 == 0):
  # If it has no floating points then its leap year, check next.
  print(f"Yeeee! {year}, is a Leap year!")
elif (year % 4 == 0) and (year % 100 != 0):
      # If it has no floating points then its leap year, and year/100 got a floating numnber its a leap year.
      print(f"Yeeee! {year}, is a Leap year!")

else:
  print("Alas, Not a leap year.")
