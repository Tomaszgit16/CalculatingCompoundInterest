# Estimated yearly interest
import sys
import math

ctype = int(input('Enter 1 for continous compounding or enter 2 for non-continous compounding: '))

#Check for invailild input

# def is_ok(a):
#     if (years<=0 or principal<=0 or interest<=0 or comp_per_year<=0):
#         print('All inputs must be positive')
#         sys.exit()


# if (ctype !=1 or ctype != 2):
#     print('Invaild input')
#     sys.exit()

#continous compounding

if ctype==1:

    print('How many year will you be saving?')
    years = int(input('Enter years: '))

    print('How much money is currently in your account?')
    principal = float(input('Enter current amount in account: '))

    print('What do you estimate will be th early interest of this investment?')
    interest = float(input('Enter interest number % example 10% = 0.1 '))

    if (years<0 or principal<0 or interest<0):
        print('All inputs must be positive')
        sys.exit()

    amount =  principal*math.e**(interest*years)
    print('Final amount', amount)

#continous compounding

if ctype==2:


    print('How many year will you be saving?')
    years = int(input('Enter years: '))

    print('How much money is currently in your account?')
    principal = float(input('Enter current amount in account: '))

    print('What do you estimate will be th early interest of this investment?')
    interest = float(input('Enter interest number % example 10% = 0.1 '))

    comp_per_year = float(input('Enter the number of times the interest is compounded per year: '))

    amount =  principal*(1+interest/comp_per_year)**(comp_per_year*years)
    print('Final amount', amount)