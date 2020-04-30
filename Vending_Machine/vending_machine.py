# Name: Michael Lochner
# Section: CIS 115 Spring 2020
# Project: VendingMachine
# Description: A Vending Machine that 'dispenses' three types of drinks. (resembles a Finite State Machine)

#-------------------------------------PASSWORD = 42--------------------------------------------------------------------------
import time

# Variables
state = 'A' # maintains state of machine
total_Inserted = 0.00 # amount of money the user has inserted
drink_1 = 2 # number of type 1 drinks
drink_2 = 4 # number of type 2 drinks
drink_3 = 1 # number of type 3 drinks
cost = 1.00

# Loop for Vending Machine
i = 0
while i < 1:
    if state == 'A':
        # Start the vending Machine
        start = input("Type 'start' to wake up the vending machine or 'exit' to power down or 'restock' to restock: ")
        if start == 'start':
            state = 'B' 
        elif start == 'exit':
            state = 'G'  
        elif start == 'restock':
            state = 'F' 
        
    elif state == 'B':
        # Insert money
        insert_money = input("Enter amount of money or type 'refund' for your money back: ")
        if insert_money == 'refund':
            state = 'E'
        else:
            insert_money = float(insert_money.strip('$'))
            total_Inserted += insert_money
            print("You have inserted $" + str('{:0,.2f}'.format(total_Inserted)) + " out of the cost of: $" + str('{:0,.2f}'.format(cost)))
            if total_Inserted >= cost:
                state = 'C'

    elif state == 'C':
        # Choose a drink
        drink = input("Type which drink you want (i.e. 1, 2, or 3) or type 'refund' for your money back: ")
        
        if drink == '1':
            if drink_1 == 0:
                print("Sorry, we are out of those.")
            else:
                print("There are " + str(drink_1) + " of those drinks left")
                drink_1 -= 1
                state = 'D'
        elif drink == '2':
            if drink_2 == 0:
                print("Sorry, we are out of those.")
            else:
                print("There are " + str(drink_2) + " of those drinks left")
                drink_2 -= 1
                state = 'D'
        elif drink == '3':
            if drink_3 == 0:
                print("Sorry, we are out of those.")
            else:
                print("There are " + str(drink_3) + " of those drinks left")
                drink_3 -= 1
                state = 'D'
        elif drink == 'refund':
            state = 'E'
        

    elif state == 'D':
        # Dispense a drink
        print("Dispensing Drink")
        total_Inserted -= 1.00

        if total_Inserted == 0:
            print("No change required. Thank You")
            state = 'A'
        else:
            state = 'E'


    elif state == 'E':
        # Return Money
        print("Returning Change: $" + str('{:0,.2f}'.format(total_Inserted)))
        total_Inserted = 0
        state = 'A'

    elif state == 'F':
        # Restocking
        password = input("Enter password to allow for restocking: ")

        if password == '42':
            print("Restocking Machine...")
            i = 0
            while i < 3:
                time.sleep(.5)
                print(".")
                i += 1
            i = 0
            drink_1 = 2
            drink_2 = 4
            drink_3 = 1
            print("Machine Restocked")
            state = 'A'
        else:
            print("WRONG PASSWORD")
            state = 'A'

    elif state == 'G':
        # Power Down Machine
        password = input("Enter password to allow for power down: ")

        if password == '42':
            print("Powering down:")
            print("3")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("1")
            time.sleep(1)
            print("GOOD-BYE WORLD")
            break
        else:
            print("WRONG PASSWORD")
            state = 'A'

    else:
        print("invalid state")
        break