"""Advanced Task
@author Gabriela Melo
@since 06/03/2015
@modified 13/03/2015
"""

"""
@pre possible receives a size 4 puzzle, containing, in string format, 1 to 15 and X
@post returns True if it's possible to solve the puzzle and False if it's not 
"""
def possible(user):  
    puzzle = [[' 1', ' 2', ' 3', ' 4'],
              [' 5', ' 6', ' 7', ' 8'], 
              [' 9', '10', '11', '12'], 
              ['13', '14', '15', ' X']]
    size = 4
    count = xi = xj = i = j = 0

    for i in range(size-1):
        for j in range(size-1):
            if (user[i][j] == ' X' or user[i][j] == 'X'):
                xi = i
                xj = j

    c_distance = 3-xi + 3-xj

    for i in range(size):
        for j in range(size):
            if (i == xi and j == xj):
                if(puzzle[i][j] != ' X'):
                    count += 1
            elif(puzzle[i][j] == ' X'):
                nothing = 0
            elif (int(puzzle[i][j]) != int(user[i][j])):
                count += 1

    if((count+c_distance)%2 == 0):
        return True   
    else:
        return False

user = [[' 1', ' 2', ' 3', ' 4'],
        [' 5', ' 6', ' 7', ' 8'], 
        [' 9', '10', '11', '12'],
        ['13', '14', '15', ' X']]
size = 4
 
for i in range(size):
        for j in range(size):
            user[i][j] = str(input('Add item in position [' + str(i) + '][' + str(j) + ']: ' ))
for a in user:
    print(a)

if(possible(user)):
    print("It's possible to put it back to the standard configuration")
else:
    print("It's impossible to put it back to the standard configuration")
