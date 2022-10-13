#Programming: Estimating the number of primes less than x Write a program to count how many 
#primes are less than 10, 100, 1,000, ..., 100,000,000. Fit a curve to your data and estimate 
#the number of primes less than x, where x is a positive integer.


def prime_numbers(n):
    primes = []
    for i in range(2, n + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i%j == 0:
                break
        else:
            primes.append(i)
    return primes


n= int(input('What is your number?'))
prime_list = prime_numbers(n)
print(prime_list)