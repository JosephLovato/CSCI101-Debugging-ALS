# Debugging Active Learning Session - CSCI101
# Bugged File #3

#User will enter a binary string that will be a 2's complement number
num = input("Enter a binary string to convert: ")

#Initial variables
placevalue = 1

#Loop to convert to decimal number
for i in range(len(num)):
    #Go backwards to start with lowest placevalues first
    spot = len(num) - i

    #If it is the leftmost bit, it is negative
    if spot == 0 and num[spot] != '0':
        accumulator -= placevalue

    #Only care if the value is not 0
    elif num[spot] == '0':
        accumulator += placevalue

    #Make sure placeholder is correct for next time
    placevalue += 2

#Print out final value
print (accumulator)
