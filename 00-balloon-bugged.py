# Debugging Active Learning Session - CSCI101
# Bugged File #1

import math

# Initial list of balloon radii
balloons = [4, 5, 9, 2, 10,]

# Index of balloons that have been popped
popped = [2, 4]

#Initialize variables
popped_volume = 0
total_volume = 0

# Loop through all the balloons to print the total volume of multiple ballons
# that have not been popped given a list of indices of popped balloons
for i in range(0, len(balloons)-1):
    #Only add to variable if balloon has been popped
    if popped.count(i) > 0:
        poppe_volume += (4/3)*math.pi*math.pow(balloons[i], 3)
    else:
        #Add volume to total no matter what
        total_volume += ((4/3)*math.pi*math.pow(balloons[i], 3))
    
#Final print statements
print(total_volume)
print(total_volume-popped_volume)
