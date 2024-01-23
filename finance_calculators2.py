import math

"""
START

PART 1 

Display intro message to user
Ask the user to select the investment or bond pathway.
Get user to select either investment or bond
User needs to select either the Investment or Bond calculator. 
Remove the case sensitivity from the user option, the user can proceed if the word is correc

PART 2

For investment, ask user for deposit amount, interest rate, the number of investment years planned and whether simple of compound interest

PART 3 

Calculate simple VS compound interest using the 'interest' variable
‘r’ is the interest entered above divided by 100, e.g. if 8% is entered,
then r is 0.08.
● ‘P’ is the amount that the user deposits.
● ‘t’ is the number of years that the money is being invested.
● ‘A’ is the total amount once the interest has been applied

The formula to calculate the simple interest: A = P *(1 + r*t)

The formula to calculate the compound interest: A = P * math.pow((1+r),t)

PART 4

Create home loan repayment calculator
For bond, ask user for:
1) The present value of the house. 
2) The interest rate.
3) The number of months they plan to take to repay the bond.

Use the following formula: repayment = (i * P)/(1 - (1 + i)**(-n))
‘P’ is the present value of the house.
‘i’ is the monthly interest rate, calculated by dividing the annual
interest rate by 12. Remember to divide the interest entered by
the user by 100 e.g. (8 / 100) before dividing by 12.
● ‘n’ is the number of months over which the bond will be repaid.

Print out the repayment amount

STOP

"""

# Intro message
LINE = "-" * 100

print(LINE)
print()
print("To select the correct calculator, please see the definitions of the calculators below ")
print("Investment - to calculate the amount of interest you'll earn on your investment ")
print("Bond - to calculate the amount you'll have to pay on a home loan ")
print()
print(LINE)

# User selects 'investment' or 'bond' pathway

while True:
    user_option = input("Please enter either 'investment' or 'bond' from the menu above to proceed: ")


    if user_option.lower() == "investment":
        print("You have selected the Investment calculator")
        deposit = int(input("What is your deposit amount (£)? "))
        interest_rate = float(input("Enter the interest rate (as a whole number, not percentage): "))
        rate = (interest_rate/100) 
        years = int(input("Enter the number of years you plan to invest for: "))

        while True:
            interest = (input("Do you want 'simple' or 'compound' interest? "))

        # Calculate amount gained using simple or compound interest (dependent on user's selection) 
        
            if interest.lower() == "simple":
                    total_amount = (deposit *(1 + (rate * years)))
                    print('Your total interest will be: £{:.2f}'.format(total_amount)) # print out amount to 2 decimal places
                    break
            elif interest.lower() == "compound":
                    total_amount = (deposit * (math.pow((1+rate),years)))
                    print('Your total interest will be: £{:.2f}'.format(total_amount))
                    break
            else:
                print("Error.")
                # print(input("Please enter 'simple' or 'compound'."))
        break        

    elif user_option.lower() == "bond":
        print("You have selected the Home loan repayment calculator")
        # Calculate the home loan repayment amount
        house_value = int(input("Please enter the present value of your house (£): "))
        annual_rate = float(input("Enter the interest rate (as a whole number, not percentage): "))
        time = int(input("Enter the number of months you plan to to take to repay the bond: "))
        monthly_rate = ((annual_rate/100)/12)
        repayment =  ((monthly_rate*house_value)/(1 - ((1+monthly_rate)**(-time))))  # repayment = (i * P)/(1 - (1 + i)**(-n))
        print("Your repayment amount is " + '£{:.2f}'.format(repayment))
        break
    else:
        print("Error! You have selected an invalid option.")
        
        
        
    print(" ")


   







