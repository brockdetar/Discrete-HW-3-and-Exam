

def hextobin():
    hex1 = input('What would you like to convert to binary?\n')
    hex1int = int(hex1, base=16)
    result = bin(hex1int)
    print (result)
    
def bintohex():
    bin1 = int(input('What would you like to convert from binary to hexadecimal?\n'))
    result = hex(bin1)
    print (result)




















user_input = int(input('1 for Hexa to binary or 2 for binary to Hexa.\n'))

if user_input == 1:
    hextobin()
    #print ('hello')
elif user_input == 2:
    bintohex()
    
    