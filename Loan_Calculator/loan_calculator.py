# Name: Michael Lochner
# Section: CIS 115 Spring 2020
# Description: Payment Calculator for your loan.

# Gets input from user for loan calculation
principal_str = (input("Enter principal amount borrowed: "))
years = float(input("Enter number of years required to repay loan: "))
rate_str = (input("Enter the interest rate on the loan (as a percentage): "))

# Converts strings to floats
principal = float(principal_str.strip('$'))
rate = float(rate_str.strip('%')) / 100

# Calculates annual loan payment
payment = (((1+rate)**years)*principal*rate)/(((1+rate)**years)-1)

# Converts and outputs annual loan payment
annual_payment = '{:0,.2f}'.format(payment)
print("Annual Payment = $" + annual_payment)

# Converts and outputs monthly loan payments
monthly = payment / 12.0
monthly_payment = '{:0,.2f}'.format(monthly)
print("Monthly Payment = $" + monthly_payment)

# Converts and outputs total loan payments
total = payment * years
total_amount_to_pay = '{:0,.2f}'.format(total)
print("Total paid for the life of the loan = $" + total_amount_to_pay)

# Receives annual income from user and converts to monthly income
annual_income_str = (input("Enter your annual income: "))
annual_income = float(annual_income_str.strip('$'))
monthly_income = annual_income / 12

# Outputs if you made a good choice with this loan
if monthly > monthly_income:
    if rate > 0.05:
        print("You should refinance. Your monthly payments exceed your monthly income.\n")
    else:
        print("You should seek financial counseling.\n")
else:
    print("With your monthly income exceeding the monthly payments, you should be able " 
          "to pay off the loan in time as long as you make all the payments.\n")

