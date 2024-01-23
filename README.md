# Finance-Calculator
Capstone Project - Variables and Control Structures

## Task Description

PART 1 

Display intro message to user
Ask the user to select the investment or bond pathway.
Get user to select either investment or bond
User needs to select either the Investment or Bond calculator. 
Remove the case sensitivity from the user option, the user can proceed if the word is correct

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