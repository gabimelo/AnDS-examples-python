"""Hall of Fame
@author Gabriela Melo
@since 06/03/2015
@modified 13/03/2015
"""

def possible(user):  
    puzzle = [[' 1', ' 2', ' 3', ' 4'],
              [' 5', ' 6', ' 7', ' 8'], 
              [' 9', '10', '11', '12'], 
              ['13', '14', '15', ' X']]
    size = 4
    count = 0

    for i in range(size):
        for j in range(size):
            if (puzzle[i][j] != user[i][j]):
                count += 1

    count -= 1

    i=j=0

    while (puzzle[i][j] != ' X'):
        i+= 1
        j+= 1

    c_distance = 3-i + 3-j

    if((count+c_distance)%2 == 0):
        return True
    elif(count == -1):
        return True    
    else:
        return False

possibility = False

while(possibility == False):
     
    from random import shuffle
    x = [' 1', ' 2', ' 3', ' 4',' 5', ' 6', ' 7', ' 8', 
	 ' 9', '10', '11', '12', '13', '14', '15', ' X']
    shuffle(x)

    puzzle = [[' 1', ' 2', ' 3', ' 4'],
	      [' 5', ' 6', ' 7', ' 8'], 
	      [' 9', '10', '11', '12'], 
	      ['13', '14', '15', ' X']]

    for i in range(4):
        for j in range (4):
            puzzle[i][j] = x[i*4+j]
	    
    possibility = possible(puzzle)

for a in puzzle:
    print(a)
