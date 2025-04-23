import math
import sys

# ---- WELCOME TO THE TERMINAL----
input("Welcome, press enter to continue...")
# ---- Introduction Channel ----
welcome = "Hello, and welcome to the SLC Aiport 🛬"
law = "There are a couple of rules that you must follow..."
rules1 = "Rule 1:"
rules2 = "Rule 2:"
bomb = 'NO BOMBS💣'
dld = 'MUST HAVE VALID ID🪪'
# ---- Execution of Introduction ----
print(welcome)
print(f"{law:>50}")
print(f"{rules1}{bomb:>20}")
print(f"{rules2}{dld:>30}")
agreement = input("Do you agree to the terms? (y/n):")
# ---- term agreement ---- Security Check!
if agreement == 'y' or agreement == 'Y':
    bomb = input("Do you have any bombs with you? (y/n):")
    if bomb == "y" or bomb == "Y":
        print("CALL THE FBI THIS GUY IS A TERRORIST")
        sys.exit("YOU HAVE BEEN ARRESTED")
    elif bomb == 'n' or bomb == 'N':
        ID = input("Do you have a valid ID? (y/n):")
        if ID == "y" and bomb == "n":
            welcome = "WELCOME TO SLC AIRPORT 🛬"
            print(f"{welcome:>40}")
        else:
            print("You need a valid ID in order to proceed.")
            sys.exit('YOU HAVE BEEN DENIED ENTRY')
else:
    sys.exit("YOU MUST AGREE TO TERMS AND CONDITIONS IN ORDER TO PROCEED FORWARD")
# ---- BAG CHECK KIOSK ---- 
input("Press enter to continue...")
kiosk = "Welcome to the BAG CHECK Kiosk 💼"
print(f"{kiosk:>40}")
name = input("What is your name? ")
ticket = input("Welcome do you have ticket? (each ticket is $299) (y/n):")
bag = input(F"and {name} are you checking in a bag today? (y/n):")
if bag == "y" and ticket == "y":
    weight = float(input("How much does your bag weigh? (we charge $7.99 per Lbs): "))
    total = weight * 7.99
    print(f"Thank you {name} your totals is (excluding ticket): ${total}")
    payment = float(input("Enter your payment: "))
    change = payment - total
    if payment > total:
        print(f"Thank you! Your change is: {round(change, 2)}")
        sys.exit(f"ENJOY YOUR FLIGHT {name}!")
    else:
        print("You do not have enough money!")
elif bag == "n" and ticket == "y":
    sys.exit(f"Thank you {name} have a safe flight!")
elif bag == "y" and ticket =="n":
    weight = float(input("How much does your bag weigh? (we charge $7.99 per Lbs): "))
    total = weight * 7.99 + 299
    print(f"Thank you {name} your totals is (including ticket): ${round(total,2 )} Dollar/s")
    payment = float(input("Enter your payment: "))
    change = payment - total
    if payment > total:
        print(f"Thank you! Your change is: {round(change, 2)} Dollar/s")
        sys.exit(f"ENJOY YOUR FLIGHT {name}!")
    else:
        sys.exit("You do not have enough money!")
else:
    print("We charge $299 for a ticket...")
    payment = float(input("Enter your payment: "))
    total = 299
    change = payment - total
    if payment > total:
        print(f"Thank you! Your change is: {round(change, 2)} Dollar/s")
        sys.exit(f"ENJOY YOUR FLIGHT {name}!")
    else:
        sys.exit("You do not have enough money!")


