print("Welcome to Lɛməˈneɪd Corner!")
cup_size = input("Your Lɛməˈneɪd size Sir/Mam?\nS, M, or L\n")
add_blacksalt = input("Do you want to add some Black Salt?\nY or N\n")
extra_mint = input("Do you want extra mint?\nY or N\n")
bill = 0

if cup_size == "S":
    bill += .75
elif cup_size == "M":
    bill += 1
else:
    bill += 1.25

if add_blacksalt == "Y":
    if cup_size == "S":
        bill += .25
    else:
        bill += .5

if extra_mint == "Y":
    bill += .3

print(f"Here's your COOL<FRESH<Lemonade\nThe total bill is: ${bill}.")
