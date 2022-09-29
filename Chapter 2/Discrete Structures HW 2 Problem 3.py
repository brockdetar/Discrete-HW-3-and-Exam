#describe an algorithm that checks to see if a string is a palindrome


def get_input():
    print ('Please type your possible palindrome')
    palindrome = input()
    palindrome = palindrome.lower()
    return palindrome


def check(palindrome):
    rev = []
    for i in palindrome:
        rev.insert(0, i)
        
    #palindrome = palindrome.lower()
    checkpal = list(palindrome)
    print (checkpal)
    if rev == checkpal:
        print(palindrome , 'is a palindrome')
    else:
        print('not a palindrome')
    
    
    



palindrome = get_input()

result = check(palindrome)