#Discrete Structures Exam 5
#Write a program to count and print all the different ways
#there are to choose half a dozen donuts from
#3 varieties at a donut shop.
#Repeat the exercise for a full dozen with 21 varieties.
import random
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement


donuts = ['Chocolate' , 'Glazed' , 'Strawberry']
special_donuts = ['Chocolate' , 'Glazed' , 'Strawberry' , 'Bluebery' , 'Coconut', 'Cinnamon' , 'Maple' , 'Crumb' , 'Sugar' , 'Powder' , 'Fruit Filled' , 'Cream filled',\
                  'Jelly filled', 'Boston Cream' , 'Donut Holes' , 'Cronut' , 'Old Fashioned' , 'Long John Glazed' , 'Long John Chocolate' , 'Long John Strawberry',\
                      'Long John Maple']
count = 0
def randbox():
    amount = 12

    box = []

    for i in range(amount):
        n = random.randint(0,2)
        selected = donuts[n]
        box.append(selected)
    print(box)
    
def allposs(donuts,count):
    perm = permutations((donuts))
    for i in list(perm):
        print(i)
        count = count + 1
    print (count)
    
    
def randomdozen(donuts,count):
    comb = combinations_with_replacement((donuts), 12)
    for i in list(comb):
        print(i)
        count = count + 1
    print (count)
    
def randomdozen21(special_donuts, count):
    comb = combinations_with_replacement(special_donuts, 12)
    for i in list(comb):
        #print(i)
        count = count + 1
    print (count)
        
        
        


allposs(donuts,count)
randomdozen(donuts,count)
randomdozen21(special_donuts, count)