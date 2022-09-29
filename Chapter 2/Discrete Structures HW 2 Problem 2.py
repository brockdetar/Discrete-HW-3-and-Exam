
import random


def list_creation():
    list_length = random.randint(1,10)
    new_list = []
    for index in range(list_length):
        num = random.randint(1,100)
        new_list.append(num)
    return new_list

def strip_evens(new_list):
    evens = []
    for i in new_list:
        if i % 2 == 0:
            evens.append(i)
    print(evens)
    return evens

    


new_list = list_creation()
print (new_list)
evens = strip_evens(new_list)
print (evens)
if evens == []:
    print ('no evens')
else:
    max1 = (max(evens))
    print('The largest even is' , max1)