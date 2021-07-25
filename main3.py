# Estimated yearly interest
import sys
import math

print('How many year will you be saving?')
years = int(input('Enter years: '))

# If years < 0:
#     print('You cant print years below 0')
#     sys.exit()

print('How much money is currently in your account?')
principal = float(input('Enter current amount in account: '))

print('How much money do you plan on investing monthly?')
monthly_invest = float(input('Enter amount: '))

print('What do you estimate will be th early interest of this investment?')
interest = float(input('Enter interest number % example - 10 = 10%: '))
#real_interest = interest * 0.01

#monthly_invest = monthly_invest * 12
final_amount = 0
# print('This is how much money you would have in your account after {} years: ').format(years) + str(final_amount)
i=1
if (years<0 or principal<0 or interest<0):
    print('All inputs must be positive')
    sys.exit()

amount =  principal*math.e**(interest*years)
print('Final amount', amount)

# print(f'{0}', principal * (1 + real_interest))
#
#
#
# for i in range(i, years):
#
#     if i < years:
#
#
#     #if final_amount == 0:
#         #final_amount = principal
#         final_amount = (final_amount + monthly_invest) * (1 + real_interest)
#
#         print(f'{i}',final_amount)
