print("Welcome to Lɛməˈneɪd Corner!")
cup_size = input("Your Lɛməˈneɪd size Sir/Mam?\nS, M, or L\n")
add_blacksalt = input("Do you want to add some Black Salt?\nY or N\n")
extra_mint = input("Do you want extra mint?\nY or N\n")

lemon = ("""
                       .-.
                      /  .|
                    .' .  .'.
                 .-'. .    . '-._
               .' ..    . . . .  '.
              /. .    .        .  .|
             / .  . .     . .. . .  |
            |. .  .      .. . . ...  |
            / . .     .       .  .  . |
           | . . ._______ .. . .  . ..|
           |   . /  Your \ .   . .  . |
           |. . { Lemonade}. ..   . ..|
           |.  . \_enjoy_/.     .   ..|
           | .  .          . . . . .  |
           |. .     .    .. .   .   ..|
            \  . .        .  . .  . . /
            |  .  .      .  .  . . . |
             \. .     .  . .  .. . .'
              \  ..      .. .   . /
               ':_ .  .  . ... _.'
                  '-.. . .  .-'
                      '._..'   
""")
print(lemon)

if cup_size == "s":
    bill = .75
    # print(f"Your small pizza will be ${bill}")
    if add_blacksalt == "y":
        bill += .5
        # print(f"final bill ${bill}")
    if extra_mint == "y":
        bill += 1
    print(f"Here's your COOL<FRESH<Lemonade\n ${bill}.")

if cup_size == "m":
    bill = 1
    # print(f"Your small pizza will be ${bill}")
    if add_blacksalt == "y":
        bill += .5
        # print(f"final bill ${bill}")
    if extra_mint == "y":
        bill += 1
    print(f"Here's your COOL<FRESH<Lemonade\n ${bill}.")

if cup_size == "l":
    bill = 1.25
    # print(f"Your small pizza will be ${bill}")
    if add_blacksalt == "y":
        bill += .5
        # print(f"final bill ${bill}")
    if extra_mint == "y":
        bill += 1
    print(f"Here's your COOL<FRESH<Lemonade\n ${bill}.")


