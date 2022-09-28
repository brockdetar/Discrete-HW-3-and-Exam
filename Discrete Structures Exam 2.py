#Use the cashier's algorithm. Develop a program that randomly selects a total charge. Then 
#randomly select a payment in dollars and cents that exceeds that charge. Then have the 
#program calculate the change in pennies, nickels, dimes, quarters, ones, fives, and twenties. 
#Bonus points for anyone who writes a program that can "Count change back."
import random

def chargeandpayment():
    charge = random.uniform(1.00, 100.00)
    fcharge = ("{:.2f}".format(charge))
    payment = random.uniform(charge,100.00)
    fpay = ("{:.2f}".format(payment))
    change = (float(fpay)) - charge
    fchange = ("{:.2f}".format(change))
    print('Total charge is ', fcharge, '\n You paid with ', fpay, '\n Change is ' ,fchange, )
    return(fchange)
    

def exact_change(change):
    change = (float(change))
    if change == 0:
        print('No change')
    elif (change) < 0:
        print('No change')
    elif 100 <= (change):
        print ('1 100 dollar bill')
        change = change - 100
        change = "{:.2f}".format(change)
        exact_change(change)
        print (change)
    elif 50 <= (change):
        print ('1 50 dollar bill')
        change = change - 50
        change = "{:.2f}".format(change)
        print (change)
        exact_change(change)
    elif 20 <= (change):
        print('1 20 dollar bill')
        change = change - 20.00
        change = "{:.2f}".format(change)
        print(change)
        exact_change(change)
    elif 10<= (change):
        print('1 10 Dollar Bill')
        change = change - 10.00
        change = "{:.2f}".format(change)
        print(change)
        exact_change(change)
    return (change)

def coins(change):
        print('f', change)
        
        x = change
        D = 100
        q = 25
        d = 10
        n = 5
        dollars = (x - (x % D))/D
        money1= x % D
        numberQ = (money1 - (money1 % q))/q
        money2 = x % q
        numberD = (money2 - (money2 % d))/d
        money3 = money2 % d
        numberN = (money3 - (money3 % n))/n
        pennies = money3 % n
        return int(numberQ), int(numberD), int(numberN), pennies , int(dollars)
        
        
       
        
      


change = chargeandpayment()
change = exact_change(change)
num = 100
change = int(num * (change))
print ('z',change)
numberQ, numberD, numberN, pennies , dollars = coins(change)
print ('change')

if dollars == 0:
    print('No dollars')
elif dollars == 1:
    print('1 dollar')
elif dollars > 1:
    print(dollars, 'Dollars')
if numberQ == 0:
    print('No Quarters')
elif numberQ == 1: 
    print('1 Quarter')
elif numberQ > 1:
    print(numberQ, ('Quarters'))
if numberD == 0:
    print('No Dimes')
elif numberD == 1: 
    print('1 Dime')
elif numberD > 1:
    print(numberD, ('Dimes'))
if numberN == 0:
    print('No Nickels')
elif numberN == 1: 
    print('1 Nickels')
elif numberN > 1:
    print(numberN, ('Nickels'))
if pennies == 0:
    print('No pennies')
elif pennies == 1: 
    print('1 penny')
elif pennies > 1:
    print(pennies, ('Pennies'))