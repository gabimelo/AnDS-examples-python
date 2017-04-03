puzzle = [[' 1', ' 2', ' 3', ' 4'],[' 5', ' 6', ' 7', ' 8'], [' 9','10', '11', '12'], ['13', '14', '15', ' X']]
size = 4

for a in puzzle:
    print(a)

i=j=0

while (puzzle[i][j] != ' X'):
    i+= 1
    j+= 1

play = input('Do you want to make a move [y/n]: ')

while (play == 'y'):
	
    move = input('Choose movement [u/d/l/r]: ')
    valid = 'true'

    if (move == 'u'):
        if (i == size - 1):
            valid = 'false'
            print('Invalid movement')
        if (valid == 'true'):
            puzzle[i][j] = puzzle[i+1][j]
            puzzle[i+1][j] = ' X'
            i+= 1
    elif (move == 'd'):
        if (i == size + 1):
            valid = 'false'
            print('Invalid movement')
        if (valid == 'true'):
            puzzle[i][j] = puzzle[i-1][j]
            puzzle[i-1][j] = ' X'
            i-= 1
    elif (move == 'l'):
        if (j == size - 1):
            valid = 'false'
            print('Invalid movement')
        if (valid == 'true'):
            puzzle[i][j] = puzzle[i][j+1]
            puzzle[i][j+1] = ' X'
            j+= 1
    elif (move == 'r'):
        if (j == size + 1):
            valid = 'false'
            print('Invalid movement')
        if (valid == 'true'):
            puzzle[i][j] = puzzle[i][j-1]
            puzzle[i][j-1] = ' X'
            j-= 1
    else:
        print('Invalid movement')

    for a in puzzle:
        print(a)

    play = input('Do you want to make another move [y/n]: ')
