import random
continue_flipping = True

print("Welcome to the CoinFlip script! To begin, please press ENTER.")

while continue_flipping:
    while True:
        input("PRESS ENTER TO FLIP")
        result = random.choice(("Heads", "Tails"))
        print(result)
        again = input("Would you like to continue flipping? (y/n): ")
        if again.lower() != "y":
            continue_flipping = False
            break