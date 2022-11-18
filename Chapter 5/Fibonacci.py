#Compare the number of operations and the time needed
#to compute Fibonacci numbers recursively versus that
#needed to compute them iteratively

import time


def fib_recursive(n):
    global count
    count += 1
    if n <= 1:
        return n 
    else: 
        return fib_recursive(n -1) + fib_recursive(n-2)
    
        
        
        




def fib_iterative(fib):
    N = 35
    global count
    for i in range(2,N):
        count += 1
        new = fib[i-1] + fib[i-2]
        fib.append(new)
    return fib
        
    




count = 0

print ('Recursive or Iterative')
user_input = input()
if user_input == 'Recursive':
    start = time.time()
    for i in range (1,35):
        print (fib_recursive(i))
    end = time.time()
    print ('It took {}'.format(count))
    print ('It took ' , end - start, ('seconds'))
    
elif user_input == 'Iterative':
    fib = [0,1]
    start = time.time()
    fib_iterative(fib)
    end = time.time()
    print (fib)
    print ('It took {}'.format(count))
    print ('It took ', end - start, 'seconds')
    

    