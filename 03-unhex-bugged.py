# Debugging Active Learning Session - CSCI101
# Bugged File #4

#Making dictionary for conversion, this code is correct
hexdict = {'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
for i in range (0, 10):
    hexdict[str(i)] = i

user_input = ""
while user_input != "quit" and user_input != "q":
    #Get user input and initialize variable
    user_input = input("> ")
    ans = 0

    # Sometimes hex numbers are prefixed with "0x", ex. "0xfff" to show that they are hex.
    # We want this function to work regardless of whether this prefix is there or not.
    # So, if the prefix is there, we just remove it.
    if user_input[:2] == "0x":
        user_input = user_input[1:]

    done = True
    for i in range (0, len(user_input)):
        position_power = 16**(len(user_input)-1-i)
        if not (user_input[i] in hexdict):
            print("You entered an invalid character")
            done = True
            break
        curr_digit = hexdict[user_input[i]]
        ans += curr_digit * position_power

    if done:
        break
    else:
        print(ans)
