# Debugging Active Learning Session - CSCI101
# Bugged File #5

import random

sz = 20 # the size of the board


# initialize mines_list
mines_list = []
for i in range(0, sz):
    mines_list.append([])
    for j in range (0, sz):
        mines_list[i].append(False)

# randomly place some mines   
for k in range (0, 75):
    y = random.randint(0, sz-1)
    x = random.randint(0, sz-1)
    mines_list[y][x] = True

#given a 2D list of bools, create a 2D list where each element

ncount = []
# make ncount the same size as input mines_list
for i in range(0, sz):
    ncount.append([])
    for j in range (0, sz):
        ncount[i].append(0)
# count up each cell's True neighbors
for y in range(0, sz):
    for x in range (0, sz)):
        if (mines_list[y-1][x-1] == True):
            ncount[y][x] += 1
        if (mines_list[y-1][x] == True):
            ncount[y][x] += 1
        if (mines_list[y-1][x+1] == True):
            ncount[y][x] += 1
     
        if (mines_list[y][x-1] == True):
            ncount[y][x] += 1
        if (mines_list[y][x+1] == True):
            ncount[y][x] += 1

        if (y < sz-1):
            if (x > 0) and (mines_list[y+1][x-1] == True):
                ncount[y][x] += 1
            if (mines_list[y+1][x] == True):
                ncount[y][x] += 1
            if (x < sz-1) and (mines_list[y+1][x+1] == True):
                ncount[y][x] += 1

#print board
for i in range (0, sz):
        for j in range (0, sz):
            if (mines_list[i][j] == True):
                print('X', end=' ')
            else:
                print(ncount[i][j], end=' ')
        print('\n', end="")

