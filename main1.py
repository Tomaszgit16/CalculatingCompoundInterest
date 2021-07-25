# Estimated yearly interest
import sys

start_over = 'True'
while start_over == 'True':

    print('How many year will you be saving?')
    years = int(input('Enter years: '))

    print('How much money is currently in your account?')
    principal = float(input('Enter current amount in account: '))

    print('How much money do you plan on investing monthly?')
    monthly_invest = float(input('Enter amount: '))

    print('What do you estimate will be th early interest of this investment?')
    interest = float(input('Enter interest number % example - 10 = 10%: '))
    real_interest = interest * 0.01

    #monthly_invest = monthly_invest * 12
    final_amount = 0



    i = 1
    print(f'Year {i} : ', round(float((principal) * (1+real_interest)), 5),' zł')
    while i < years:
        principal = (principal + monthly_invest) * (1+real_interest)
        i = i + 1
        print(f'Year {i} : ', round(principal, 5), ' zł')
    redo_program = input('To restart type y or to quit type any key ')

    if redo_program == 'y':
         start_over = 'True'
    else:
         start_over = 'null' #means false quit program