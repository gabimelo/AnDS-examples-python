"""Task 3
@author Gabriela Melo
@since 06/03/2015
@modified 13/03/2015
"""

puzzle = [[' 1', ' 2', ' 3', ' 4'],
          [' 5', ' 6', ' 7', ' 8'], 
          [' 9', '10', '11', '12'], 
          ['13', '14', '15', ' X']]
size = 4

for a in puzzle:
    print(a)

i=j=3

quit = False

while not quit:
	
    move = input('Choose movement [u/d/l/r] or quit[q]: ')

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
