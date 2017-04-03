"""Hall of Fame
@author Gabriela Melo
@since 06/03/2015
@modified 13/03/2015
"""

"""
@pre possible receives a size 4 puzzle, containing, a list with items in string type, from 1 to 15 and X
@post returns True if it's possible to solve the puzzle and False if it's not 
"""
def possible(user): 
    # standard  puzzle is used to check how many swaps are going to be necessary
    puzzle = [[' 1', ' 2', ' 3', ' 4'],
              [' 5', ' 6', ' 7', ' 8'], 
              [' 9', '10', '11', '12'], 
              ['13', '14', '15', ' X']]
    size = 4
    count = 0

    # count is incremented whenever a number on the input puzzle is different from the standard
    for i in range(size):
        for j in range(size):
            if (puzzle[i][j] != user[i][j]):
                count += 1
    
    # number of swaps needed is one less than the amount of different numbers
    count -= 1

    i=j=0
    
    # we need to find the position of X to get the city-distance
    for a in range(4):
        for b in range(4):
            if (user[a][b] == ' X'):
                i = a
                j = b

    c_distance = 3-i + 3-j

    # puzzle is solvable when sum of number of swaps and city-distance of X is even
    if((count+c_distance) % 2 == 0):
        return True
    # if there is no different numbers, puzzle can be (and already is) solved
    elif(count == -1):
        return True    
    else:
        return False


"""
@post returns a size 4 puzzle that can be solved
"""
def create_puzzle():
    possibility = False

    # loop runs while a possible configuration hasn't been found
    while(possibility == False):
     
        # first a list from 1 to 15 and X is shuffled
        from random import shuffle
        x = [' 1', ' 2', ' 3', ' 4',' 5', ' 6', ' 7', ' 8', 
	     ' 9', '10', '11', '12', '13', '14', '15', ' X']
        shuffle(x)

        # then it is turned into a list of lists, to have the correct puzzle format
        puzzle = [[' 1', ' 2', ' 3', ' 4'],
	          [' 5', ' 6', ' 7', ' 8'], 
	          [' 9', '10', '11', '12'], 
	          ['13', '14', '15', ' X']]
        for i in range(4):
            for j in range (4):
                puzzle[i][j] = x[i*4+j]
	
        # then the solvability of this configuration is checked    
        possibility = possible(puzzle)

    return puzzle


# beginning of main program

puzzle = create_puzzle()

for a in puzzle:
    print(a)

# we need to find the position of X
for a in range(4):
        for b in range(4):
            if (puzzle[a][b] == ' X'):
                i = a
                j = b

quit = False

while not quit:
	
    move = input('Choose movement [u/d/l/r] or quit[q]: ')

    # analises the movement, checking if it is possible (not possible to move X out of the puzzle)
    # if possible, swaps X with the other number and updates the position of X (i,j)
    if (move == 'd'):
        if (i == size - 1):
            print('Invalid movement')
        else:
            puzzle[i][j] = puzzle[i+1][j]
            puzzle[i+1][j] = ' X'
            i+= 1
    elif (move == 'u'):
        if (i == size + 1):
            print('Invalid movement')
        else:
            puzzle[i][j] = puzzle[i-1][j]
            puzzle[i-1][j] = ' X'
            i-= 1
    elif (move == 'r'):
        if (j == size - 1):
            print('Invalid movement')
        else:
            puzzle[i][j] = puzzle[i][j+1]
            puzzle[i][j+1] = ' X'
            j+= 1
    elif (move == 'l'):
        if (j == size + 1):
            print('Invalid movement')
        else:
            puzzle[i][j] = puzzle[i][j-1]
            puzzle[i][j-1] = ' X'
            j-= 1
    elif (move == 'q'):
        quit = True
    else:
        print('Invalid movement')

    for a in puzzle:
        print(a)